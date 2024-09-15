1. 打印“Hello, World!”：print("Hello, World!")
2. 变量赋值和使用：message = "Welcome to Python!"
print(message)
3. 列表（List）操作：numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6)
print(numbers)
4. 条件语句（if-else）：age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
5. 循环（for loop）：for i in range(5):
    print(i)
6. 函数定义：def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
7. 读取文件：with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
8. 异常处理：try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
9. 导入模块：import math
print(math.sqrt(16))
10. 类和对象：class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

person = Person("Bob", 30)
person.introduce()
