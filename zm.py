import time

# 定义一个无限循环，每秒更新输出
while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"\r当前时间：{current_time}", end="", flush=True)
time.sleep(1)

   


   
