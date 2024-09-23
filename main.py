import pyautogui
import pygetwindow as gw
import time

import windowUtils as wu

import random

# 输出分辨率
screenWidth, screenHeigth = pyautogui.size()
print(screenWidth,screenHeigth)


print(pyautogui.onScreen(5000,500))
# 判断坐标是否在屏幕上，是的话返回true。

# pyautogui.moveTo(736,18,0)
# pyautogui.mouseDown()
# pyautogui.moveTo(736,600,0)
currentMousex , currentMousey = pyautogui.position()
print(currentMousex,currentMousey)
# 提示框
# pyautogui.alert('hello','alert')

# pyautogui.scroll(-100)
# 获取所有活动窗口
all_windows = gw.getAllWindows()

# 打印所有窗口的标题和几何信息
title = ""
for window in all_windows:
    if 'Edge' in window.title:
        title = window.title
        print("Edge进程:"+title)
        # edge浏览器
        edge_windows = gw.getWindowsWithTitle(title)
        for window in edge_windows:

            print('窗口是不是全屏:', window.isMaximized)
            # 获取edge浏览器窗口的位置
            edge_window_rect = wu.get_windows_pos(title)
            print(edge_window_rect)
            time.sleep(1)
            print(window.isActive)
            window.activate()

            pyautogui.moveTo(edge_window_rect[0],edge_window_rect[1])
            pyautogui.move(100,100)
            currentMousex, currentMousey = pyautogui.position()
            print(currentMousex, currentMousey)
            wu.loopOperate(title)

    # else:
    #     print(window.title)

# 生成两个1到10的随机整数
random_number_1 = random.randint(1, 10)
random_number_2 = random.randint(1, 10)

# 打印结果
print("随机数1:", random_number_1)
print("随机数2:", random_number_2)

def windowOper(title):

    edge_windows = gw.getWindowsWithTitle(title)
    edge_window_rect = edge_windows[0].left, edge_windows[0].top, edge_windows[0].width, edge_windows[0].height
    print(edge_window_rect)

#
#
# def switch_to_edge():
#     # 微信
#     edge_windows = gw.getWindowsWithTitle('微信')
#
#     # 获取微信窗口的位置
#     edge_window_rect = edge_windows[0].left, edge_windows[0].top, edge_windows[0].width, edge_windows[0].height
#     print(edge_window_rect)
#
#     # 将微信窗口按住鼠标左键拖动到0,0位置
#     if edge_windows:
#
#         edge_window = edge_windows[0]
#         print(edge_window.isActive)
#         edge_window.activate()
#
#
#         pyautogui.mouseDown(edge_window_rect[0]+10, edge_window_rect[1]+10)
#         pyautogui.moveTo(100,100)
#         pyautogui.mouseUp()
#
#         edge_window.activate()
#         pyautogui.moveTo(521, 649)
#         # 鼠标左键点击
#         # 设置输入的文本
#
#         text = "你号"
#         print(edge_window.isActive)
#         pyautogui.write(text)
#         time.sleep(2)
#         pyautogui.press("enter")
#
#
#
# # 调用函数
# # switch_to_edge()
#
#
#
#





















