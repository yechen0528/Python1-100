from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid
"""
使用单进程的方法下载,下载完一个数据后才会开始下载第二个文件
def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
"""


def download_task(filename):
    # getpid()函数可以获取进程的识别码
    print(f'启动下载进程，进程号{getpid()}.')
    print(f'开始下载{filename}...')
    # 模拟下载时间,从5-10秒钟随机取值
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename}下载完成! 耗费了{time_to_download}秒')


def main():
    """
    使用多进程的方式下载文件,两者同时进行,不用排队
    :return:
    """
    start = time()
    p1 = Process(target=download_task, args=('这是一个元组,代表传递给函数的参数',))
    p1.start()
    p2 = Process(target=download_task, args=('元组中仅一个参数用,结尾',))
    p2.start()
    # join函数表示等待进程结束
    p1.join()
    p2.join()
    end = time()
    print(f'总共耗费了{end - start}秒')


counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end="", flush=True)
        counter += 1
        sleep(0.1)


def main_task():
    """
    设置两个进程,一个输出ping一个输出pong.
    counter并非两个进程共享,两个进程各输出了10次,若需要进程之间共享参数需要使用 multiprocessing模块中的Queue类
    :return:
    """
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main_task()
