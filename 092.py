print("哈喽")
print("游戏开始")
import random 

random_number = random.randint(1, 6)  # 生成1到6之间的随机整数
print(random_number)  # 使用圆括号而非花括号来调用print函数
print("  1  2  3  4  5  6  回到起点  7  8  9  10   +5  ")

# 使用一个 if 语句检查 random_number 是否等于 6，并在其中嵌套 print 语句
if random_number == 6:
    print("：：：：：：：；：：：：：：：：：6")
if random_number == 5:
    print("：：：：：：：：：：：：：5")
if random_number == 4:
    print("：：：：：：：：：：4")
if random_number == 3:
    print("： ：：：：：：3")
if random_number == 2:
    print("：：：：：2")
if random_number == 1:
    print("：：：1")