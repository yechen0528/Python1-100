from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('这是一个元组',))
    t1.start()
    t2 = Thread(target=download, args=('这是第二',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'总共耗费了{end - start}秒')


class DownloadTask(Thread):
    """
    继承Thread类
    """
    def __init__(self, filename):
        # 继承父类的所有的init方法
        super().__init__()
        # self._xxxx 约定为类内部的实现细节,不应该直接访问(但是可以访问)
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def task_main():
    start = time()
    t1 = DownloadTask(filename="第一个")
    t1.start()
    t2 = DownloadTask(filename="第二个")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'总共耗费了{end - start}秒')


if __name__ == '__main__':
    task_main()
