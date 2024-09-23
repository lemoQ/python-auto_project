'''
@SDK功能描述：鼠标轨迹
'''

import ctypes
import os
import sys

# 创建句柄
key = "SNKJuSrrrTnQ5UXYr4zr6XEveL7V2jg2X9h5BHGS5Des"  # 字符串
key_bytes = key.encode('utf-8')  # 将字符串转换为 bytes

# 设置模型文件路径
onnx = "d://SNTrack.onnx"  # 字符串
onnx_bytes = onnx.encode('utf-8')  # 将字符串转换为 bytes

# 假设 DLL 文件名为 SNSDK.dll
sn_sdk = ctypes.WinDLL('d://SNSDK.dll')


# 定义 SN_RESULT 结构体
class SN_RESULT(ctypes.Structure):
    _fields_ = [("code", ctypes.c_int),
                ("message", ctypes.c_char * 4096)]


# 定义 SN_POINT 结构体
class SN_POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]


# 定义 SN_POINT_PARAMS 结构体
class SN_POINT_PARAMS(ctypes.Structure):
    _fields_ = [("point", SN_POINT),
                ("delayTime", ctypes.c_int)]


# 定义函数原型
sn_sdk.apiSNCreateHandle.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char),
                                     ctypes.POINTER(SN_RESULT)]
sn_sdk.apiSNCreateHandle.restype = ctypes.c_void_p

sn_sdk.apiSNGetVersion.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
sn_sdk.apiSNGetVersion.restype = SN_RESULT

sn_sdk.apiSNMouseMove.argtypes = [ctypes.c_void_p, SN_POINT, SN_POINT, ctypes.POINTER(SN_POINT_PARAMS)]
sn_sdk.apiSNMouseMove.restype = SN_RESULT  # 根据实际情况调整

sn_sdk.apiSNDestroyHandle.argtypes = [ctypes.c_void_p]
sn_sdk.apiSNDestroyHandle.restype = SN_RESULT

result = SN_RESULT()  # 创建 SN_RESULT 实例
handle = sn_sdk.apiSNCreateHandle(key_bytes, onnx_bytes, ctypes.byref(result))
if result.code != 0:
    message = result.message.decode('gbk', errors='replace').strip()
    print("Result message:", message)
else:
    print("Handle created successfully")

# 获取版本号
version = ctypes.create_string_buffer(4096)
version_result = sn_sdk.apiSNGetVersion(handle, version)
if version_result.code != 0:
    message = result.message.decode('gbk', errors='replace').strip()
    print("Result message:", message)
else:
    message = result.message.decode('gbk', errors='replace').strip()
    print("Result message:", version.value.decode())

# 获取轨迹
# 定义开始和结束坐标
start_point = SN_POINT(100, 100)
end_point = SN_POINT(800, 800)

# 假设返回的轨迹点数量
num_points = 4096

# 创建一个数组来接收轨迹点
points_array = (SN_POINT_PARAMS * num_points)()

# 调用 apiSNMouseMove 函数
move_result = sn_sdk.apiSNMouseMove(handle, start_point, end_point, points_array)

# 检查结果
if move_result.code != 0:
    message = result.message.decode('gbk', errors='replace').strip()
    print("Result message:", message)
else:
    # 遍历并打印每个点
    for i in range(num_points):
        if points_array[i].point.x == -1 and points_array[i].point.y == -1:
            break  # 轨迹结束
        print(
            f"Point {i}: ({points_array[i].point.x}, {points_array[i].point.y},{points_array[i].delayTime})")  # X坐标 ,Y坐标 ,延时时间

# 释放句柄
destroy_result = sn_sdk.apiSNDestroyHandle(handle)
if destroy_result.code != 0:
    message = result.message.decode('gbk', errors='replace').strip()
    print("Result message:", message)
else:
    print("Handle destroyed successfully")

'''
输出鼠标轨迹如下：
Handle created successfully
Result message: 1.0
Point 0: (100, 100,0)
Point 1: (100, 98,10)
Point 2: (103, 98,15)
Point 3: (111, 98,16)
Point 4: (116, 101,15)
Point 5: (122, 104,2)
Point 6: (129, 107,13)
Point 7: (135, 109,2)
Point 8: (144, 112,14)
Point 9: (155, 117,2)
Point 10: (167, 123,14)
Point 11: (180, 128,2)
Point 12: (193, 134,13)
Point 13: (209, 138,2)
Point 14: (225, 144,13)
Point 15: (238, 149,5)
Point 16: (254, 157,10)
Point 17: (269, 162,5)
Point 18: (282, 168,11)
Point 19: (298, 175,5)
Point 20: (311, 180,10)
Point 21: (326, 185,6)
Point 22: (341, 193,9)
Point 23: (369, 211,15)
Point 24: (396, 231,16)
Point 25: (419, 251,16)
Point 26: (442, 270,16)
Point 27: (461, 285,17)
Point 28: (481, 300,15)
Point 29: (491, 311,15)
Point 30: (502, 319,2)
Point 31: (513, 329,14)
Point 32: (523, 343,2)
Point 33: (535, 355,14)
Point 34: (546, 369,0)
Point 35: (558, 383,15)
Point 36: (570, 397,2)
Point 37: (582, 411,13)
Point 38: (596, 427,2)
Point 39: (608, 443,14)
Point 40: (620, 459,5)
Point 41: (633, 476,10)
Point 42: (645, 490,5)
Point 43: (656, 503,11)
Point 44: (666, 515,5)
Point 45: (675, 527,11)
Point 46: (684, 538,5)
Point 47: (694, 551,11)
Point 48: (702, 565,5)
Point 49: (710, 577,11)
Point 50: (716, 588,5)
Point 51: (723, 598,11)
Point 52: (728, 606,5)
Point 53: (733, 615,11)
Point 54: (738, 622,5)
Point 55: (743, 631,11)
Point 56: (747, 637,5)
Point 57: (750, 644,11)
Point 58: (753, 652,5)
Point 59: (756, 659,10)
Point 60: (759, 666,5)
Point 61: (761, 673,11)
Point 62: (764, 680,5)
Point 63: (766, 687,11)
Point 64: (768, 694,5)
Point 65: (769, 701,10)
Point 66: (771, 708,5)
Point 67: (772, 714,11)
Point 68: (773, 722,5)
Point 69: (774, 729,10)
Point 70: (777, 743,16)
Point 71: (778, 755,15)
Point 72: (778, 764,16)
Point 73: (780, 775,16)
Point 74: (781, 784,16)
Point 75: (781, 785,15)
Point 76: (781, 789,2)
Point 77: (781, 790,13)
Point 78: (781, 792,2)
Point 79: (782, 796,14)
Point 80: (782, 796,2)
Point 81: (782, 797,14)
Point 82: (782, 798,15)
Point 83: (782, 800,311)
Point 84: (784, 800,16)
Point 85: (784, 800,5)
Point 86: (785, 800,10)
Point 87: (786, 800,5)
Point 88: (786, 800,11)
Point 89: (788, 800,6)
Point 90: (789, 800,9)
Point 91: (790, 800,5)
Point 92: (791, 800,10)
Point 93: (793, 800,16)
Point 94: (795, 800,16)
Point 95: (796, 800,15)
Point 96: (797, 800,15)
Point 97: (797, 800,2)
Point 98: (798, 800,15)
Point 99: (798, 800,30)
Point 100: (799, 800,15)
Point 101: (799, 800,15)
Handle destroyed successfully
Process finished with exit code 0
'''