# number_guesser.py
import random
"""
数字猜谜游戏
电脑随机生成1~100整数，你来猜，提示大了还是小了，直到猜对，统计次数
"""
def guess_game():
    ans = random.randint(1, 100)
    count = 0
    print("🎮 猜数字游戏！我想好了1～100之间一个整数。")

    while True:
        try:
            user = int(input("请输入你猜的数字："))
            count += 1
            if user > ans:
                print("太大啦，往小一点试试！")
            elif user < ans:
                print("太小啦，往大一点试试！")
            else:
                print(f"🎉恭喜！猜对了！一共猜了 {count} 次")
                break
        except ValueError:
            print("❌只能输入整数！")

if __name__ == "__main__":
    guess_game()