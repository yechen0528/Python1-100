import subprocess
import schedule
import time


def restart_server():
    print("将在 {} 重启服务器...".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    # subprocess.run()  执行命令 shutdown  /r表示重启  /t表示超时执行 0表示 0秒后执行,即立即执行
    subprocess.run(["shutdown", "/r", "/t", "0"])


def restart_process(path_name="各个工具配置数据.txt"):
    process_name = path_name  # 替换为你的进程名
    print(f"重启进程 {process_name}...")

    try:
        # 停止进程    capture_output=True 以管理员身份运行
        subprocess.run(["taskkill", "/IM", process_name, "/F"], check=True, capture_output=True)

        # 启动进程（替换为启动进程的命令）
        subprocess.run([path_name], check=True)

        print(f"进程 {process_name} 重启成功！")
    except subprocess.CalledProcessError as e:
        print(f"进程 {process_name} 重启失败：{e}")


# 设置重启时间，24小时制
restart_time = "17:37"

# 定义定时任务     在重启时间restart_time,这里是 03:00时,执行函数
# schedule.every().day.at(restart_time).do(restart_server)
schedule.every().day.at(restart_time).do(restart_process)

while True:
    # schedule.run_pending()函数会运行那些已经到达执行时间的任务
    schedule.run_pending()
    time.sleep(1)


