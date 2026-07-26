# -*- coding: utf-8 -*-
# GitHub深度学习每日打卡：梯度下降+迭代轨迹可视化
# 仅依赖numpy、matplotlib，适配D盘Anaconda base环境
import numpy as np
import matplotlib.pyplot as plt

# ===================== 1. 定义目标函数与梯度 =====================
def loss_func(x, y):
    """待优化二元凸函数：f(x,y) = (x-3)² + (y+1)²
    全局最小值点：(3, -1)，最小值为0
    """
    return (x - 3) ** 2 + (y + 1) ** 2

def compute_gradient(x, y):
    """手动求偏导计算梯度"""
    dx = 2 * (x - 3)
    dy = 2 * (y + 1)
    return np.array([dx, dy])

# ===================== 2. 梯度下降迭代核心逻辑 =====================
def gradient_descent(start_pos, lr=0.1, max_iter=500, threshold=1e-6):
    pos = np.array(start_pos, dtype=np.float64)
    track_history = [pos.copy()]  # 保存每一步坐标，用于绘图

    for i in range(max_iter):
        grad = compute_gradient(pos[0], pos[1])
        grad_norm = np.linalg.norm(grad)

        # 梯度足够小时提前收敛退出
        if grad_norm < threshold:
            print(f"迭代{i}次完成收敛")
            break

        # 梯度下降更新公式：沿梯度反方向移动
        pos = pos - lr * grad
        track_history.append(pos.copy())

    return pos, np.array(track_history)

# ===================== 3. 执行优化并绘制等高线轨迹 =====================
if __name__ == "__main__":
    # 超参数配置
    start_point = [0.0, 0.0]
    learning_rate = 0.1

    # 运行梯度下降
    best_pos, history = gradient_descent(start_point, lr=learning_rate)

    # 打印结果
    print("="*60)
    print(f"迭代终点坐标：x={best_pos[0]:.4f}  y={best_pos[1]:.4f}")
    print(f"最终损失值：{loss_func(best_pos[0], best_pos[1]):.6f}")
    print(f"理论最优解：x=3，y=-1")
    print("="*60)

    # 绘制等高线+迭代路径
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    # 生成网格
    x_range = np.linspace(-2, 6, 200)
    y_range = np.linspace(-4, 2, 200)
    X, Y = np.meshgrid(x_range, y_range)
    Z = loss_func(X, Y)

    # 绘制等高线
    plt.figure(figsize=(9, 7))
    contour = plt.contour(X, Y, Z, levels=30, cmap="coolwarm")
    plt.clabel(contour, inline=True, fontsize=8)

    # 绘制下降轨迹
    plt.plot(history[:, 0], history[:, 1], "o-", color="#ff4444", linewidth=2, markersize=4, label="梯度下降迭代轨迹")
    # 标记起点、终点、理论最小值
    plt.scatter(start_point[0], start_point[1], c="blue", s=80, label="迭代起点")
    plt.scatter(best_pos[0], best_pos[1], c="green", s=80, label="迭代收敛点")
    plt.scatter(3, -1, c="gold", s=120, marker="*", label="理论全局最小值")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("梯度下降迭代轨迹可视化 | 深度学习优化基础")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
