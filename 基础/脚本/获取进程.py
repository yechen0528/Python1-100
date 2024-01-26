import psutil


def get_running_processes():
    # 获取所有正在运行的进程信息
    running_processes = psutil.process_iter(['pid', 'name'])

    # 输出每个进程的 PID 和名称
    for process in running_processes:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}")


if __name__ == "__main__":
    get_running_processes()
