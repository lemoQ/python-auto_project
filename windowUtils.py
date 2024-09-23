import time

import pyautogui
import win32gui,win32con,win32api,win32print
from PIL import ImageGrab

# 声明一个全局int 变量,左右偏移
global_int_left = 300

# 声明一个全局int 变量,上下偏移
global_int_up = 483

def get_windows_pos(name):
    handle = win32gui.FindWindow(0, name)
    if (handle == 0):
        return 0
    # 计算屏幕缩放比
    hDC = win32gui.GetDC(0)
    # 100%下真实的屏幕高度
    real_w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    apparent_w = win32api.GetSystemMetrics(0)
    # 以上代码分别获取了屏幕的真实宽度和缩放之后的宽度
    # print(real_w,apparent_w)
    scale_radio = real_w / apparent_w
    # 根据这两个值可以计算出缩放比
    # print(scale_radio)
    origin_window_react = win32gui.GetWindowRect(handle)
    fixed_window_react = [item * scale_radio for item in origin_window_react]
    # 计算窗口坐标的正确位置
    return fixed_window_react

def loopOperate(title):
    # 按五次ctrl+tab键
    for i in range(5):
        edge_window_rect = get_windows_pos(title)
        pyautogui.moveTo(edge_window_rect[0], edge_window_rect[1])
        print('开始操作:',i)
        window_left = edge_window_rect[0];
        if i==0:
            pyautogui.move(200, global_int_up)
            print(pyautogui.position())
            time.sleep(0.5)
            print('鼠标右键点击')
            pyautogui.rightClick()
            time.sleep(0.5)
            print('按下ESC')
            pyautogui.press('esc')
            print('操作结束:', i)
            window_left = pyautogui.position()[0]
        else:
            pyautogui.move(window_left + i*global_int_left,global_int_up )
            print(pyautogui.position())

            time.sleep(0.5)
            print('鼠标右键点击')
            pyautogui.rightClick()
            time.sleep(0.5)
            print('按下ESC')
            pyautogui.press('esc')
            print('操作结束:',i)

        # pyautogui.hotkey('ctrl', 'tab')