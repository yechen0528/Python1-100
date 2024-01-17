import os
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DOWNLOAD_PATH = 'images/'


def download_picture(picture_url: str):
    """
    下载保存图片
    :param picture_url: 图片的URL
    """
    filename = picture_url[picture_url.rfind('/') + 1:]
    resp = requests.get(picture_url)
    with open(os.path.join(DOWNLOAD_PATH, filename), 'wb') as file:
        file.write(resp.content)


# 检索下载的目录是否存在 如果不存在 则新建一个目录
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)
# 自动打开浏览器
browser = webdriver.Chrome()
browser.get('https://image.so.com/z?ch=beauty')
browser.implicitly_wait(10)
# 通过css选择器找到了一个具有 name属性为 q 的输入框
kw_input = browser.find_element(By.CSS_SELECTOR, 'input[name=q]')
# 在q的输入框中输入 关键词
kw_input.send_keys('苍老师')
# 模拟回车键 触发搜索
kw_input.send_keys(Keys.ENTER)
# 使用循环滚动页面,执行JavaScript代码模拟滚动浏览网页的行为
for _ in range(10):
    browser.execute_script(
        'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    )
    time.sleep(1)
# 通过css选择器找到了所有<div>标签下的<img>元素
imgs = browser.find_elements(By.CSS_SELECTOR, 'div.waterfall img')
# 创建一个最大并发数为32的线程池,命名为 pool
with ThreadPoolExecutor(max_workers=32) as pool:
    # 遍历所有的 图片 元素
    for img in imgs:
        # 提取图片元素的 src 数据(即图片的url)
        pic_url = img.get_attribute('src')
        # 使用 下载保存 函数,通过 url 下载图片到本地
        pool.submit(download_picture, pic_url)