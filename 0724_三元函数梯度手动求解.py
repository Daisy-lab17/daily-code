# 导入数值计算库numpy，用于组装梯度向量与打印格式
import numpy as np

"""
任务说明：
目标三元函数 f(x,y,z) = x² + 2y² + 3z²
梯度定义：梯度是由函数对每个自变量的偏导数构成的向量
∇f = [∂f/∂x , ∂f/∂y , ∂f/∂z]
偏导数计算规则：对某一变量求导时，其余变量全部视作常数
"""

# 定义原三元目标函数
def func_3var(x, y, z):
    """
    输入：三个自变量x、y、y
    返回：函数f(x,y,z)的计算结果
    """
    term1 = x ** 2       # x平方项
    term2 = 2 * (y ** 2) # 2倍y平方项
    term3 = 3 * (z ** 2) # 3倍z平方项
    return term1 + term2 + term3

# 手动计算三个偏导数，组装梯度向量
def calculate_gradient(x, y, z):
    # 对x求偏导：d(x²)/dx = 2x，y、z为常数导数为0
    partial_x = 2 * x
    # 对y求偏导：d(2y²)/dy = 4y，x、z为常数导数为0
    partial_y = 4 * y
    # 对z求偏导：d(3z²)/dz = 6z，x、y为常数导数为0
    partial_z = 6 * z

    # 将三个偏导数组合成梯度向量（列向量/行向量形式）
    grad_vector = np.array([partial_x, partial_y, partial_z])
    return grad_vector

# 程序入口，测试运行
if __name__ == "__main__":
    # 自定义一组测试坐标点，可自行修改数值测试
    x_test, y_test, z_test = 2, 3, 4

    # 计算函数在该点的函数值
    f_value = func_3var(x_test, y_test, z_test)
    # 计算该点处完整梯度向量
    grad_result = calculate_gradient(x_test, y_test, z_test)

    # 格式化打印结果
    print("===== 三元函数梯度计算结果 =====")
    print(f"函数 f(x,y,z) = x²+2y²+3z²")
    print(f"计算坐标点：x={x_test}, y={y_test}, z={z_test}")
    print(f"该点函数值 f = {f_value:.2f}")
    print(f"梯度向量 ∇f = [∂f/∂x , ∂f/∂y , ∂f/∂z] = {grad_result}")