"""
PyAutoGUI桌面小工具
模拟键盘输入、获取屏幕信息，简单桌面自动化演示
第三方库：pyautogui
"""
import pyautogui
import time

# 安全设置：鼠标移到屏幕左上角会终止程序，防止失控
pyautogui.FAILSAFE = True

def show_mouse_info():
    """获取鼠标当前位置、屏幕分辨率"""
    screen_width, screen_height = pyautogui.size()
    mouse_x, mouse_y = pyautogui.position()
    print(f"屏幕分辨率：宽{screen_width} 高{screen_height}")
    print(f"当前鼠标坐标：X={mouse_x}, Y={mouse_y}")


def auto_text_input(text: str, wait_second: int = 5):
    """
    自动输入文本
    :param text: 需要输入的字符串
    :param wait_second: 倒计时，把光标放到输入框
    """
    print(f"倒计时 {wait_second} 秒，请把光标定位到输入框！")
    pyautogui.countdown(wait_second)
    pyautogui.write(text, interval=0.08)
    pyautogui.press("enter")
    print("文本输入完成")


if __name__ == "__main__":
    print("===== PyAutoGUI 小工具 =====")
    show_mouse_info()
    auto_text_input(text="GitHub打卡：桌面自动化pyautogui示例")