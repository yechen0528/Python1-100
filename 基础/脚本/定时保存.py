import os
import shutil
from datetime import datetime, timedelta
import schedule
import time

path = input("请输入保存文件夹路径:")
save_time = input("请输入保存时间点(参考格式23:00):")


def create_backup():
    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')

    # 构建文件夹路径
    backup_folder = os.path.join(os.getcwd(), current_date)
    print(backup_folder)

    # 如果目标文件夹已经存在，先删除它
    if os.path.exists(backup_folder):
        shutil.rmtree(backup_folder)

    # 源文件夹路径
    source_folder = os.path.join(os.getcwd(), path)

    # 复制源文件夹内容到新文件夹
    shutil.copytree(source_folder, backup_folder)

    print(f'Backup created successfully in {backup_folder}')


# 定义定时任务
schedule.every().day.at(save_time).do(create_backup)

while True:
    # 运行定时任务
    schedule.run_pending()
    time.sleep(1)
