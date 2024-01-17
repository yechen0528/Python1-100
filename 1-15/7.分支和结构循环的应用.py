from random import randint


def craps_game(money=1000):
    """
    CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
    该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
    简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出其他点数则玩家继续摇骰子，
    (第二轮)如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负
    :param money:
    :return:
    """
    money = money
    while money > 0:
        print(F"你目前的资产为:{money}")
        # 每次循环开始,将 go_on的状态初始化为 False
        go_on = False
        while True:
            """
            若资产money>0，则向下执行
            """
            debt = int(input("请输入下注金额:"))
            # 如果下注金额大于0且小于当前财产,则跳出下注循环,向下执行
            if 0 < debt <= money:
                break
            else:
                print(f"下注金额不合理,你当前总资产为{money}")
        # 第一次投骰子
        # 用 1-6 的随机数模拟骰子的点数,将两次的随机数相加模拟2个骰子
        first = randint(1, 6) + randint(1, 6)
        print(f"第1次投骰子,数值和为:{first}")
        # 判断第一次的胜负
        if first == 7 or first == 11:
            print("玩家获胜")
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print("庄家获胜")
            money -= debt
        else:
            # 若没有分出胜负,则开始第二轮投骰子, 向下执行
            go_on = True
        # 若go_on 为True则开启第二轮
        i = 2
        while go_on:
            # 重新定义 go_on的状态,防止因为 go_on因为第一次定义为True而导致无限循环
            go_on = False
            # 投骰子
            current = randint(1, 6) + randint(1, 6)
            print(f"第{i}轮投骰子,数值和为{current}")
            # 判断第二次胜负
            if current == first:
                print("玩家获胜")
                money += debt
            elif current == 7:
                print("庄家获胜")
                money -= debt
            # 如果第二轮还未分出胜负, 则改变 go_on的状态为 True,进入第三轮,如此循环
            else:
                go_on = True
                i += 1

    # 若money<=0
    print("你破产了,游戏结束")


if __name__ == '__main__':
    craps_game()


