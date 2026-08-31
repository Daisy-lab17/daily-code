# 导入tkinter基础组件，用来做图形窗口GUI
import tkinter as tk
# 导入增强控件：输入框、按钮
from tkinter import ttk
# json模块：把待办列表保存成json文件，关闭程序数据不丢失
import json
# os模块：判断文件是否存在
import os

# 定义保存待办事项的文件名
FILE_NAME = "todo.json"

# 加载本地保存的待办数据
def load_todos():
    # 判断json文件是否已经存在
    if os.path.exists(FILE_NAME):
        # 打开文件，utf‑8防止中文乱码
        with open(FILE_NAME,"r",encoding="utf‑8") as f:
            # 将json文本转为python列表返回
            return json.load(f)
    # 文件不存在，返回空列表
    return []

# 将待办列表保存到本地json文件
def save_todos(todo_list):
    with open(FILE_NAME,"w",encoding="utf‑8") as f:
        # dump：把列表写入json文件，ensure_ascii=False支持中文，indent格式化缩进
        json.dump(todo_list,f,ensure_ascii=False,indent=2)

# 待办应用主类
class TodoApp:
    # 初始化函数，程序启动最先执行
    def __init__(self,root):
        # root代表主窗口对象
        self.root = root
        # 设置窗口标题
        self.root.title("Todo备忘录")
        # 读取本地已经保存的待办
        self.todos = load_todos()

        # 创建文本输入框，宽度40
        self.entry = ttk.Entry(root,width=40)
        # 摆放输入框，上下边距5
        self.entry.pack(pady=5)

        # 创建一个框架，用来放按钮，让按钮并排
        frame_btn = ttk.Frame(root)
        frame_btn.pack()

        # 添加按钮，点击执行self.add_todo函数
        ttk.Button(frame_btn,text="添加",command=self.add_todo).grid(row=0,column=0,padx=3)
        # 删除按钮，点击执行self.del_todo函数
        ttk.Button(frame_btn,text="删除选中",command=self.del_todo).grid(row=0,column=1,padx=3)

        # 创建列表框，展示全部待办条目
        self.listbox = tk.Listbox(root,width=50,height=10)
        self.listbox.pack(pady=8)

        # 刷新界面，把本地读取到的待办显示到窗口
        self.refresh_ui()

    # 添加待办的逻辑函数
    def add_todo(self):
        # 获取输入框内容，strip()去掉首尾空格
        text = self.entry.get().strip()
        # 如果输入不为空
        if text:
            # 添加进待办列表
            self.todos.append(text)
            # 清空输入框
            self.entry.delete(0,tk.END)
            # 保存到本地文件
            save_todos(self.todos)
            # 更新界面显示
            self.refresh_ui()

    # 删除选中条目函数
    def del_todo(self):
        # 获取当前鼠标选中的条目下标
        idx = self.listbox.curselection()
        # 判断是否选中了某一项
        if idx:
            # 根据下标删除列表中的待办
            self.todos.pop(idx[0])
            # 保存修改后的数据
            save_todos(self.todos)
            # 刷新页面
            self.refresh_ui()

    # 刷新列表显示，清空旧内容，重新渲染全部待办
    def refresh_ui(self):
        # 清空listbox全部旧条目
        self.listbox.delete(0,tk.END)
        # 循环遍历待办列表，逐条插入窗口
        for item in self.todos:
            self.listbox.insert(tk.END,item)

# 程序入口
if __name__ == "__main__":
    # 创建主窗口实例
    win = tk.Tk()
    # 实例化备忘录应用
    app = TodoApp(win)
    # 启动窗口循环，窗口保持运行，等待鼠标点击输入
    win.mainloop()