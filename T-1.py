# Created on iPad.

print("cnsjnauncxjxskadnusahxhgjxshbjxjshyuowshhjx!")
import pygame
import random
import time

# 初始化pygame
pygame.init()

# 设置窗口尺寸
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# 设置标题
pygame.display.set_caption("Draggable Squares")

# 颜色列表
colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# 方块类
class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 50

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])

    def update(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.size and self.y < mouse_pos[1] < self.y + self.size:
            self.x, self.y = mouse_pos

# 方块列表
squares = []

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下时，检查是否点击了某个方块
            for square in squares:
                square.update(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEMOTION:
            # 鼠标移动时，如果正在拖动方块，则更新位置
            for square in squares:
                square.update(pygame.mouse.get_pos())

    # 清除屏幕
    screen.fill((0, 0, 0))

    # 绘制所有方块
    for square in squares:
        square.draw()

    # 每隔5秒生成一个新方块
    if time.time() % 5 == 0:
        new_square = Square(random.randint(0, window_size[0]), random.randint(0, window_size[1]), random.choice(colors))
        squares.append(new_square)

    # 更新屏幕
    pygame.display.flip()

# 退出pygame
pygame.quit()

