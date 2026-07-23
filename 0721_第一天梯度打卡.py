import numpy as np

# 定义二元函数
def f(x1, x2):
    return 3 * x1 ** 2 + 4 * x1 * x2 + x2 ** 3

# 手动计算梯度（深度学习基础练习）
def grad_f(x1, x2):
    df_dx1 = 6 * x1 + 4 * x2
    df_dx2 = 4 * x1 + 3 * (x2 ** 2)
    return np.array([df_dx1, df_dx2])

# 程序入口，运行测试
if __name__ == "__main__":
    x1, x2 = 2, 1
    func_value = f(x1, x2)
    gradient = grad_f(x1, x2)
    print(f"函数计算结果：{func_value:.2f}")
    print(f"梯度向量结果：{gradient}")
