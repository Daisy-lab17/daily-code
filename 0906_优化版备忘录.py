# -*- coding: utf-8 -*-
"""
GUI备忘录工具
依赖库：customtkinter
功能：新增、查看、删除备忘录，数据json持久化
"""
import customtkinter as ctk
import json
import os

# 保存文件
FILE_PATH = "memo_data.json"

# 加载备忘录
def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 保存备忘录
def save_data(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

class MemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("备忘录")
        self.geometry("520x450")
        ctk.set_appearance_mode("system") # 跟随系统深色/浅色模式

        self.memo_list = load_data()

        # 输入框
        self.entry = ctk.CTkEntry(self, placeholder_text="输入备忘录内容...", width=400)
        self.entry.pack(pady=12)

        # 按钮行
        self.frame_btn = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_btn.pack(pady=5)

        self.btn_add = ctk.CTkButton(self.frame_btn, text="添加", command=self.add_memo)
        self.btn_add.grid(row=0, column=0, padx=6)
        self.btn_del = ctk.CTkButton(self.frame_btn, text="删除最后一条", command=self.del_last)
        self.btn_del.grid(row=0, column=1, padx=6)
        self.btn_refresh = ctk.CTkButton(self.frame_btn, text="刷新列表", command=self.show_list)
        self.btn_refresh.grid(row=0, column=2, padx=6)

        # 文本显示区
        self.textbox = ctk.CTkTextbox(self, width=460, height=280)
        self.textbox.pack(pady=15)
        self.show_list()

    def add_memo(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.memo_list.append(text)
        save_data(self.memo_list)
        self.entry.delete(0, ctk.END)
        self.show_list()

    def del_last(self):
        if len(self.memo_list) == 0:
            return
        self.memo_list.pop()
        save_data(self.memo_list)
        self.show_list()

    def show_list(self):
        self.textbox.delete("0.0", ctk.END)
        if not self.memo_list:
            self.textbox.insert("0.0", "暂无备忘录")
            return
        for i, item in enumerate(self.memo_list, 1):
            self.textbox.insert(ctk.END, f"{i}. {item}\n")

if __name__ == "__main__":
    app = MemoApp()
    app.mainloop()