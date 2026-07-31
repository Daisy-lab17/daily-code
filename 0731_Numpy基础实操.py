import numpy as np

# 1. 创建数组
# 一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print("一维数组：", arr1)
print("数组形状：", arr1.shape)
print("数组数据类型：", arr1.dtype)

# 二维矩阵
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("\n二维矩阵：\n", arr2)
print("矩阵行列数：", arr2.shape)

# 快速生成特殊数组
zero_arr = np.zeros((2, 3))  # 全0矩阵
one_arr = np.ones((3, 2))    # 全1矩阵
range_arr = np.arange(0, 10, 2)  # 0到10步长2
print("\n全0矩阵：\n", zero_arr)
print("全1矩阵：\n", one_arr)
print("等差数组：", range_arr)

# 2. 基础运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\n数组加法：", a + b)
print("数组乘法：", a * b)
print("数组平方：", a ** 2)

# 3. 矩阵运算
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print("\n矩阵点乘：\n", np.dot(mat1, mat2))

# 4. 统计函数
print("\n数组最大值：", arr1.max())
print("数组最小值：", arr1.min())
print("数组平均值：", arr1.mean())
print("数组总和：", arr1.sum())

# 5. 切片取值
print("\n取前3个元素：", arr1[:3])
print("取矩阵第二行：", arr2[1, :])
print("取矩阵第一列：", arr2[:, 0])