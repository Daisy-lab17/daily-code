# 导入依赖库
import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class MusicPlayer:
    def __init__(self, root_window):
        # 主窗口基础配置
        self.root = root_window
        self.root.title("简易音乐播放器 | GitHub打卡项目")
        self.root.geometry("480x320")
        self.root.resizable(False, False)

        # 初始化音频引擎pygame
        pygame.init()
        pygame.mixer.init()

        # 播放器全局变量
        self.music_folder = ""    # 音乐文件夹路径
        self.music_list = []      # 全部歌曲列表
        self.current_index = 0    # 当前播放歌曲下标
        self.is_playing = False   # 是否正在播放
        self.is_pause = False     # 是否暂停

        # 搭建GUI界面组件
        self.build_ui()

    def build_ui(self):
        """构建图形化界面"""
        # 歌曲列表框
        self.list_box = tk.Listbox(self.root, width=60, height=12)
        self.list_box.pack(pady=8)

        # 按钮容器框架
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        # 各个功能按钮
        tk.Button(btn_frame, text="选择歌曲文件夹", command=self.load_music_dir).grid(row=0, column=0, padx=3)
        self.play_btn = tk.Button(btn_frame, text="播放", command=self.play_music)
        self.play_btn.grid(row=0, column=1, padx=3)
        tk.Button(btn_frame, text="上一曲", command=self.last_song).grid(row=0, column=2, padx=3)
        tk.Button(btn_frame, text="下一曲", command=self.next_song).grid(row=0, column=3, padx=3)
        tk.Button(btn_frame, text="停止", command=self.stop_music).grid(row=0, column=4, padx=3)

        # 音量调节滑块
        volume_frame = tk.Frame(self.root)
        volume_frame.pack(pady=6)
        tk.Label(volume_frame, text="音量:").grid(row=0, column=0)
        volume_slide = tk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                 command=self.set_volume, length=300)
        volume_slide.set(50)  # 默认音量50%
        volume_slide.grid(row=0, column=1)

    def load_music_dir(self):
        """选取本地文件夹，自动读取所有mp3音乐"""
        folder = filedialog.askdirectory(title="选择存放MP3歌曲的文件夹")
        if not folder:
            return
        self.music_folder = folder
        self.music_list.clear()
        self.list_box.delete(0, tk.END)

        # 筛选后缀为mp3的音频文件
        for file in os.listdir(folder):
            if file.lower().endswith(".mp3"):
                self.music_list.append(os.path.join(folder, file))
                self.list_box.insert(tk.END, file)

        if len(self.music_list) == 0:
            messagebox.showwarning("提示", "文件夹内没有找到MP3格式歌曲！")

    def set_volume(self, value):
        """设置播放音量，value范围0~100"""
        vol = int(value) / 100
        pygame.mixer.music.set_volume(vol)

    def play_music(self):
        """播放/暂停歌曲，新开线程防止界面卡死"""
        if len(self.music_list) == 0:
            messagebox.showinfo("提示", "请先选择歌曲文件夹！")
            return

        # 暂停状态恢复播放
        if self.is_pause:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.is_pause = False
            self.play_btn.config(text="暂停")
            return

        # 新开线程播放音乐，避免GUI阻塞
        def play_thread():
            pygame.mixer.music.load(self.music_list[self.current_index])
            pygame.mixer.music.play()
            self.is_playing = True
            self.play_btn.config(text="暂停")
            # 歌曲播放完毕自动切下一首
            while pygame.mixer.music.get_busy() and self.is_playing:
                pass
            if self.is_playing and not self.is_pause:
                self.next_song()

        threading.Thread(target=play_thread, daemon=True).start()

    def last_song(self):
        """切换上一曲"""
        if not self.music_list:
            return
        self.stop_music()
        self.current_index = self.current_index - 1 if self.current_index > 0 else len(self.music_list)-1
        self.play_music()

    def next_song(self):
        """切换下一曲"""
        if not self.music_list:
            return
        self.stop_music()
        self.current_index = (self.current_index + 1) % len(self.music_list)
        self.play_music()

    def stop_music(self):
        """停止播放音乐"""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_pause = False
        self.play_btn.config(text="播放")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = MusicPlayer(main_window)
    main_window.mainloop()