import heapq


def prices():
    # 用股票价格大于100元的股票构造一个新的字典
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    dict_list = {}
    for x in prices:
        if prices[x] > 100:
            dict_list[x] = prices[x]

    print(dict_list)

    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)


def scores_dict():
    """嵌套的字典"""
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    scores = {}
    for x in names:
        scores[x] = {}
        for y in courses:
            scores[x][y] = input(f'请输入{x}的{y}成绩: ')
            print(scores)


def heapq_test():
    """heapq模块（堆排序）"""
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


if __name__ == '__main__':
    heapq_test()
