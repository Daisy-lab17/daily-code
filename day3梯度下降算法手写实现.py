# -*- coding: utf-8 -*-
# GitHub每日打卡：梯度下降算法手写实现
# 适用：人工智能/深度学习入门，最优化基础练习
import numpy as np

def target_function(x, y):
    """目标优化函数：f(x,y) = (x-3)² + (y+1)²
    理论最小值点：x=3，y=-1，最小值为0
    """
    return (x - 3) ** 2 + (y + 1) ** 2

def calculate_gradient(x, y):
    """手动求偏导，计算梯度（梯度方向是函数上升最快方向）
    对x求偏导：2*(x-3)
    对y求偏导：2*(y+1)
    """
    dx = 2 * (x - 3)
    dy = 2 * (y + 1)
    return np.array([dx, dy])

def gradient_descent_optimize(init_point, learning_rate=0.1, max_iter=300, tol=1e-6):
    """
    梯度下降核心迭代函数
    :param init_point: 迭代起点，数组 [x0, y0]
    :param learning_rate: 学习率（步长），太大震荡、太小收敛慢
    :param max_iter: 最大迭代次数，防止无限循环
    :param tol: 收敛阈值，梯度足够小时判定找到最优解
    :return: 最优坐标、迭代历史记录
    """
    # 初始化坐标与迭代记录
    current_pos = np.array(init_point, dtype=np.float64)
    history = []

    for i in range(max_iter):
        # 1. 计算当前位置梯度
        grad = calculate_gradient(current_pos[0], current_pos[1])
        grad_norm = np.linalg.norm(grad)  # 梯度模长

        # 2. 记录每一步的坐标和函数值
        loss_val = target_function(current_pos[0], current_pos[1])
        history.append({"iter": i, "pos": current_pos.copy(), "loss": loss_val})

        # 3. 收敛判断：梯度趋近于0，到达极小值点，提前终止
        if grad_norm < tol:
            print(f"迭代{i}次后收敛，梯度小于阈值，停止迭代")
            break

        # 4. 梯度下降核心公式：往梯度反方向更新坐标
        current_pos = current_pos - learning_rate * grad

    return current_pos, history

# ------------------- 程序入口运行测试 -------------------
if __name__ == "__main__":
    # 设定初始起点 (0, 0)
    start = [0.0, 0.0]
    # 执行梯度下降优化
    best_point, iter_history = gradient_descent_optimize(init_point=start)

    # 打印最终结果
    print("=" * 50)
    print(f"迭代完成，最优解坐标：x = {best_point[0]:.4f}, y = {best_point[1]:.4f}")
    print(f"目标函数最小值：{target_function(best_point[0], best_point[1]):.6f}")
    print(f"理论最优解：x=3.0，y=-1.0，最小值0")
    print("=" * 50)