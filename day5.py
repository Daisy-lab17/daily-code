"""
GitHub 每日算法打卡：梯度下降法实现
目标：求解一元二次函数 y = x² 的最小值
学习率、迭代次数可自定义，附带详细中文注释
"""

# 目标函数：y = x²
def func(x):
    return x ** 2

# 目标函数一阶导数：dy/dx = 2x
def gradient(x):
    return 2 * x

# 梯度下降核心迭代过程
def gradient_descent(start_x, learn_rate, iteration):
    x = start_x
    for i in range(iteration):
        grad = gradient(x)
        # 沿梯度反方向更新自变量
        x = x - learn_rate * grad
        # 每20轮打印一次迭代信息
        if i % 20 == 0:
            print(f"迭代轮数：{i:2d} | x值：{x:.4f} | 函数值：{func(x):.4f}")
    return x

if __name__ == "__main__":
    # 超参数设置
    initial_x = 8.0       # 初始取值点
    lr = 0.1              # 学习率
    iter_times = 100      # 总迭代次数

    print("===== 梯度下降求解 y=x² 最小值 =====")
    final_x = gradient_descent(initial_x, lr, iter_times)
    print(f"\n迭代完成，最优解 x ≈ {final_x:.4f}")
    print(f"函数最小值 y ≈ {func(final_x):.4f}")