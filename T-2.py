

import os

# 获取当前工作目录
current_dir = os.getcwd()
print("Current directory:", current_dir)

# 列出目录下的所有文件和子目录
for entry in os.listdir(current_dir):
    print(entry)

# 创建一个新目录
os.mkdir('new_directory')

# 删除一个目录
os.rmdir('new_directory')

# 更改当前工作目录
os.chdir('/path/to/new/directory')

# 获取环境变量
env_var = os.environ.get('HOME')
print("Home directory:", env_var)

# 执行系统命令
exit_code = os.system('ls -l')
print("Exit code:", exit_code)

# 获取文件大小
file_size = os.path.getsize('/path/to/file.txt')
print("File size:", file_size, "bytes")

# 获取文件修改时间
mtime = os.path.getmtime('/path/to/file.txt')
print("Last modified:", mtime)
