from time import time
from threading import Thread

import requests


# 继承Thread类创建自定义的线程
class DownloadHanlder(Thread):

    def __init__(self, url):
        # 继承父类的所有init方法
        super().__init__()
        self.url = url

    def run(self):
        # 从url中获取文件名    例:从 "https://example.com/images/photo.jpg" 中提取 出 "photo.jpg"
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(url=self.url)
        # 选择某个路径,将获取的图片保存到本地
        with open(r'D:\PyCharm\Python1-100\1-15\14picture\\' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get("https://apis.tianapi.com/game/index?key=e8f16160733bb613e2579048eb465493&num=10")
    # 从接口获取的json字符串转化为字典
    print(resp.json())
    data = resp.json()
    for x in data['result']['newslist']:
        # 获取图片的url地址
        url = x['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url=url).start()


if __name__ == '__main__':
    main()