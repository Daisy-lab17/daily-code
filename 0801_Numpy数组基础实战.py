# 导入数值计算库numpy
import numpy as np

# 1. 创建一维数组
arr1 = np.array([1, 3, 5, 7, 9])
print("一维数组：", arr1)
print("数组尺寸：", arr1.shape)
print("数组元素类型：", arr1.dtype)

# 2. 创建二维矩阵
arr2 = np.array([[2, 4, 6],
                 [1, 3, 5]])
print("\n二维矩阵：")
print(arr2)
print("矩阵行列数：", arr2.shape)

# 3. 基础运算
print("\n数组全部乘2：", arr1 * 2)
print("数组求和：", arr1.sum())
print("数组最大值：", arr1.max())
print("数组平均值：", arr1.mean())

# 4. 特殊数组生成
zero_arr = np.zeros((3, 3))  # 3行3列全0矩阵
one_arr = np.ones((2, 4))    # 2行4列全1矩阵
print("\n3*3零矩阵：")
print(zero_arr)
print("\n2*4全1矩阵：")
print(one_arr)

# 5. 切片取值
print("\n取数组第2到第4个元素：", arr1[1:4])
print("取矩阵第一行全部元素：", arr2[0, :])