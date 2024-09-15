import os
import resource
import shutil
import urllib.request
import io
import matplotlib.pyplot as plt
import socket
import subprocess
import sys
from datetime import datetime
import time
import random

class SimpleOS:
    def __init__(self):
        password = "110608"
        attempts = 3
        
        while attempts > 0:
            entered_password = input("请输入密码：")
            if entered_password == password:
                print("密码正确！欢迎使用SimpleOS。")
                break
            else:
                attempts -= 1
                print(f"密码错误！还有{attempts}次尝试机会。")
                if attempts == 0:
                    print("密码尝试次数过多，请等待30秒")
                    time.sleep(30)
                    raise Exception("密码尝试次数过多，初始化被停止。")
        
        self.commands = {
            '1': self.show_time,
            '2': self.do_math,
            '3': self.exit_os,
            '4': self.check_free_ports,
            '5': self.download_and_display_image,
            '6': self.list_directory,
            '7': self.network_ping,
            '8': self.system_info,
            '9': self.weather_query_placeholder,  # Placeholder function for weather query
            '10': self.game_guess_number,
            '11': self.create_file,
            '12': self.delete_file,
            '13': self.hardware_status,
            '14': self.search_files,
            '15': self.copy_file,
            '16': self.move_file,
            '17': self.create_directory,
            '18': self.delete_directory,
            '19': self.text_editor,
        }
        self.self_check()
        self.run()

    def self_check(self):
        steps = [
            "ROS正在加载1…",
            "ROS正在加载2…",
            "ROS正在自检3…",
            "ROS正在自检4…"
        ]
        for step in steps:
            print(step)
            time.sleep(0.7)
        print("ROS自检完成。")

    def run(self):
        while True:
            cmd = input("请输入命令: ").strip()
            if cmd in self.commands:
                self.commands[cmd]()
            elif cmd == 'ed':
                self.text_editor()
            else:
                print("命令未识别。")
    
    def show_time(self):
        print("当前时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def do_math(self):
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        operation = input("请输入运算符 (+, -, *, /): ")
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("错误：除数不能为0。")
                return
        else:
            print("无效的运算符")
            return
        print(f"结果是: {result}")

    def exit_os(self):
        print("系统退出。")
        sys.exit(0)

    def check_free_ports(self):
        def check_port(port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.bind(('localhost', port))
                    print(f"端口{port}是空闲的。")
                except OSError as e:
                    print(f"端口{port}已被占用。错误信息: {e}")

        def main():
            print("端口检查工具")
            while True:
                port_input = input("请输入端口号（输入'q'退出）: ")
                if port_input.lower() == 'q':
                    print("程序已退出。")
                    break
                try:
                    port = int(port_input)
                    if 0 <= port <= 65535:
                        check_port(port)
                    else:
                        print("请输入一个0到65535之间的有效端口号。")
                except ValueError:
                    print("无效输入，请输入一个数字。")

        if __name__ == "__main__":
            main()

    def download_and_display_image(self):
        image_url = input("请输入图片URL: ")
        try:
            with urllib.request.urlopen(image_url) as response:
                image_data = plt.imread(io.BytesIO(response.read()))
                plt.imshow(image_data)
                plt.axis('off')
                plt.show()
        except Exception as e:
            print("无法下载图片，请检查URL或网络连接。", e)

    def list_directory(self):
        path = input("请输入要列出的目录路径：")
        try:
            files = os.listdir(path)
            for file in files:
                print(file)
        except FileNotFoundError:
            print("目录不存在。")
    
    def network_ping(self):
        host = input("请输入要ping的主机名或IP地址：")
        response = subprocess.call(['ping', '-c', '4', host])
        if response == 0:
            print(f"{host} 可达。")
        else:
            print(f"{host} 不可达。")

    def system_info(self):
        # 获取进程的CPU时间
        ru = resource.getrusage(resource.RUSAGE_SELF)
        user_time = ru.ru_utime
        sys_time = ru.ru_stime
        total_time = user_time + sys_time

        # 获取进程的内存使用
        rss, vms = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, 0

        # 获取磁盘使用率
        total, used, free = shutil.disk_usage('/')
        disk_usage = (used / total) * 100

        print(f"进程CPU时间: {total_time}s")
        print(f"进程内存使用: {rss} bytes")
        print(f"磁盘使用率: {disk_usage:.2f}%")

    def weather_query_placeholder(self):
        print("天气查询功能暂时不可用。")

    def game_guess_number(self):
        number_to_guess = random.randint(1, 100)
        guess = None
        attempts = 0
        while guess != number_to_guess:
            guess = input("猜一个1到100之间的数字：")
            try:
                guess = int(guess)
                attempts += 1
                if guess < number_to_guess:
                    print("太小了！再试一次。")
                elif guess > number_to_guess:
                    print("太大了！再试一次。")
            except ValueError:
                print("请输入一个有效的整数。")
        print(f"恭喜你，猜对了！你一共尝试了{attempts}次。")

    def create_file(self):
        filename = input("请输入要创建的文件名（带路径）：")
        try:
            with open(filename, 'w') as file:
                file.write("")
            print(f"文件'{filename}'已创建。")
        except IOError as e:
            print(f"创建文件失败：{e}")

    def delete_file(self):
        filename = input("请输入要删除的文件名（带路径）：")
        try:
            os.remove(filename)
            print(f"文件'{filename}'已删除。")
        except FileNotFoundError:
            print(f"文件'{filename}'不存在。")
        except IOError as e:
            print(f"删除文件失败：{e}")

    def hardware_status(self):
        self.system_info()
        print("注意：硬件状态信息有限，CPU温度等信息可能需要额外的库或平台支持。")

    # 新增的方法
    def search_files(self):
        directory = input("请输入要搜索的目录：")
        keyword = input("请输入搜索关键词：")
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if keyword in file:
                        print(os.path.join(root, file))
        except PermissionError:
            print("无权访问此目录。")
        except FileNotFoundError:
            print("目录不存在。")

    def copy_file(self):
        src = input("请输入源文件路径：")
        dst = input("请输入目标文件路径：")
        try:
            shutil.copy2(src, dst)
            print(f"文件'{src}'已复制到'{dst}'。")
        except FileNotFoundError:
            print("源文件不存在。")
        except PermissionError:
            print("无权访问目标位置。")
        except shutil.SameFileError:
            print("源文件和目标文件相同。")

    def move_file(self):
        src = input("请输入源文件路径：")
        dst = input("请输入目标文件路径：")
        try:
            shutil.move(src, dst)
            print(f"文件'{src}'已移动到'{dst}'。")
        except FileNotFoundError:
            print("源文件不存在。")
        except PermissionError:
            print("无权访问目标位置。")

    def create_directory(self):
        directory = input("请输入要创建的目录路径：")
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"目录'{directory}'已创建。")
        except PermissionError:
            print("无权在此位置创建目录。")

    def delete_directory(self):
        directory = input("请输入要删除的目录路径：")
        try:
            shutil.rmtree(directory)
            print(f"目录'{directory}'已删除。")
        except FileNotFoundError:
            print("目录不存在。")
        except PermissionError:
            print("无权删除此目录。")

    def text_editor(self):
        filename = input("请输入要编辑的文件名（带路径）：")
        try:
            with open(filename, 'r+', encoding='utf-8') as f:
                original_content = f.read()  # 读取原始文件内容
                f.seek(0)  # 将文件指针移回到开头
                lines = original_content.splitlines(True)  # 保留换行符并分割
    
                print("原始文件内容：")
                for line in lines:
                    print(line, end='')
    
                new_lines = []
                for line in lines:
                    edited_line = input(f"编辑行 '{line.strip()}': ")
                    if edited_line == '':
                        new_lines.append(line)  # 如果没有输入，保持原样
                    else:
                        new_lines.append(edited_line + '\n')
    
                new_content = ''.join(new_lines)
    
                # 检查内容是否发生了变化
                if new_content != original_content:
                    save_changes = input("文件内容已更改，是否保存（y/n）? ")
                    while save_changes.lower() not in ['y', 'n']:
                        save_changes = input("无效输入，请输入 y 或 n：")
    
                    if save_changes.lower() == 'y':
                        f.seek(0)
                        f.write(new_content)
                        f.truncate()
                        print(f"文件'{filename}'已更新。")
                    else:
                        print(f"文件'{filename}'的更改未保存。")
                else:
                    print(f"文件'{filename}'没有变化，无需保存。")
        except FileNotFoundError:
            print("文件不存在。")
        except IOError as e:
            print(f"编辑文件失败：{e}")

        
        
            
        



if __name__ == "__main__":
    try:
        os = SimpleOS()
    except Exception as e:
        print(e)
