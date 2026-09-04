import time

"""
简易倒计时器
输入分钟数，程序开始倒计时，结束打印提示
"""
def countdown(minutes):
    # 把分钟转成总秒数
    total_seconds = int(minutes * 60)
    print(f"⏰ 开始 {minutes} 分钟倒计时！")

    while total_seconds > 0:
        # divmod：商=分钟，余数=秒
        m, s = divmod(total_seconds, 60)
        # 格式化输出 00:00
        print(f"{m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\n✅ 时间到！")

if __name__ == "__main__":
    try:
        t = float(input("请输入倒计时多少分钟："))
        countdown(t)
    except ValueError:
        print("⚠️ 请输入数字！")