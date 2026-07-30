import numpy as np

# 构造数据集
# 特征：x1,x2  标签y = 2*x1 + 3*x2 + 噪声
np.random.seed(10)
sample_num = 50
x1 = np.linspace(0, 10, sample_num) + np.random.randn(sample_num)
x2 = np.linspace(0, 5, sample_num) + np.random.randn(sample_num)
y = 2 * x1 + 3 * x2 + np.random.randn(sample_num)

# 拼接特征矩阵，增加常数项1
X = np.column_stack((np.ones(sample_num), x1, x2))
Y = y.reshape(-1, 1)

# 最小二乘法公式求解权重 W=(X^T X)^(-1) X^T Y
weights = np.linalg.inv(X.T @ X) @ X.T @ Y

# 提取系数
bias = weights[0][0]
w1 = weights[1][0]
w2 = weights[2][0]

print("====多元线性回归训练结果====")
print(f"偏置项 b = {bias:.3f}")
print(f"特征x1权重 w1 = {w1:.3f}")
print(f"特征x2权重 w2 = {w2:.3f}")
print(f"拟合公式：y = {w1:.2f}*x1 + {w2:.2f}*x2 + {bias:.2f}")

# 单样本预测函数
def predict(x1_in, x2_in):
    return bias + w1 * x1_in + w2 * x2_in

# 测试预测
test_x1, test_x2 = 6, 3
pred_y = predict(test_x1, test_x2)
print(f"\n输入 x1={test_x1},x2={test_x2} 预测值 y={pred_y:.3f}")