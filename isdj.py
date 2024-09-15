import time
from datetime import datetime

while: 
    now = datetime.now()
    print("\r当前时间：", now.strftime("%Y-%m-%d %H:%M:%S"), end="")
    time.sleep(1)
