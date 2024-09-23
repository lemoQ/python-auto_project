import tkinter as tk
import job

# 创建主窗口
app = tk.Tk()
app.title("我的第一个Tkinter界面")

# 添加标签
label = tk.Label(app, text="欢迎来到Tkinter界面!")
label.pack(pady=20)  # pady用于设置组件间的垂直间距

import tkinter as tk

# 定义一个标志变量
is_processing = False


def job_click():
    global is_processing
    # 开始处理任务前，设置标志并禁用其他按钮
    is_processing = True
    button1.config(state=tk.DISABLED)
    button2.config(state=tk.DISABLED)
    button3.config(state=tk.DISABLED)

    print("执行点击操作")
    # 模拟任务处理过程
    # 这里可以替换为实际的任务处理逻辑
    app.after(2000, complete_processing)  # 假设任务需要2秒
    print("执行点击操作完成")

def button_click():
    global is_processing
    # 开始处理任务前，设置标志并禁用其他按钮
    is_processing = True
    button1.config(state=tk.DISABLED)
    button2.config(state=tk.DISABLED)
    button3.config(state=tk.DISABLED)
    print("执行点击操作")
    # 模拟任务处理过程
    # 这里可以替换为实际的任务处理逻辑
    app.after(2000, complete_processing)  # 假设任务需要2秒
    print("执行点击操作完成")

def complete_processing():
    global is_processing
    # 任务完成后，重置标志并启用所有按钮
    is_processing = False
    button1.config(state=tk.NORMAL)
    button2.config(state=tk.NORMAL)
    button3.config(state=tk.NORMAL)


app = tk.Tk()

button1 = tk.Button(app, text="一键收菜!", command=job_click)
button1.pack(pady=10)

button2 = tk.Button(app, text="一键任务!", command=button_click)
button2.pack(pady=10)

button3 = tk.Button(app, text="一键刷道!", command=button_click)
button3.pack(pady=10)

app.mainloop()
