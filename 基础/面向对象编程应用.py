import random
from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """牌类"""
    def __init__(self, suite, face):
        # 参数 suite表示4种花色, face表示数值
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):       # 运算符重载
        # 花色相同的比较点数大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表(除大小王)
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


class Player:
    """玩家"""
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)      # 将对应的实参 cards 加入到 cards列表中

    def arrange(self):
        """对玩家获得的cards列表进行排序"""
        self.cards.sort()


if __name__ == '__main__':
    poker = Poker()
    poker.shuffle()
    players = [Player('玩家1'), Player('玩家2'), Player('玩家3'), Player('玩家4')]
    for _ in range(13):
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.arrange()
        print(f'{player.name}: ', end='')
        print(player.cards)



