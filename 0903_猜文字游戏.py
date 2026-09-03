import random
'''
小游戏：猜数字
电脑随机生成1～100整数，玩家不断猜，提示大了还是小了，直到猜对，统计次数
'''
def guess_game():
    ans = random.randint(1, 100)   # 随机生成1~100数字
    count = 0                      # 记录猜了多少次
    print("🎮 猜数字游戏开始！数字范围：1～100")

    while True:
        try:
            user_input = int(input("请输入你猜的数字："))
            count += 1

            if user_input > ans:
                print("太大啦，再小一点！")
            elif user_input < ans:
                print("太小啦，再大一点！")
            else:
                print(f"🎉恭喜你猜对啦！答案就是{ans}，一共猜了{count}次")
                break
        except ValueError:
            print("⚠️请输入一个有效的整数！")


if __name__ == "__main__":
    guess_game()