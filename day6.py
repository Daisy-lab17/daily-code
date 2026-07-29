import numpy as np
import matplotlib.pyplot as plt

# 目标函数：f(x) = x²  最简单的凸函数，用来演示梯度下降
def func(x):
    return x ** 2

# 求梯度（导数）：f'(x) = 2x
def gradient(x):
    return 2 * x

# 梯度下降核心算法
def gradient_descent(start_x, learning_rate, epoch):
    x_history = []  # 记录每一步x的变化，方便可视化
    x = start_x
    for i in range(epoch):
        grad = gradient(x)
        x = x - learning_rate * grad
        x_history.append(x)
    return x, np.array(x_history)

# 超参数设置
initial_x = 8        # 起点
lr = 0.1             # 学习率
iter_times = 30      # 迭代次数

# 执行优化
best_x, x_trace = gradient_descent(initial_x, lr, iter_times)
best_y = func(best_x)

# 打印结果
print(f"最终收敛最优值 x = {best_x:.4f}")
print(f"函数最小值 f(x) = {best_y:.4f}")

# 可视化下降轨迹
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x_range = np.linspace(-9, 9, 200)
y_range = func(x_range)

plt.figure(figsize=(10, 5))
plt.plot(x_range, y_range, color="#222222", label=r'$f(x)=x^2$')
plt.scatter(x_trace, func(x_trace), c="#ff6b6b", s=40, label="梯度下降迭代轨迹")
plt.title("一维函数梯度下降优化过程")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()