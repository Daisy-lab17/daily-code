# 导入数值计算库numpy
import numpy as np

if __name__ == "__main__":
    # 1. 创建一维、二维数组
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2], [3, 4], [5, 6]])
    print("一维数组：\n", arr1)
    print("二维数组：\n", arr2)

    # 2. 数组基础属性
    print("数组形状：", arr2.shape)
    print("数组维度：", arr2.ndim)
    print("元素总个数：", arr2.size)

    # 3. 数组四则运算（对应位置元素计算）
    add = arr1 + 2
    mul = arr1 * 3
    print("数组+2：", add)
    print("数组*3：", mul)

    # 4. 矩阵乘法运算
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[2, 0], [1, 2]])
    mat_mul = np.dot(mat1, mat2)
    print("矩阵相乘结果：\n", mat_mul)

    # 5. 常用内置函数
    print("数组最大值：", arr1.max())
    print("数组最小值：", arr1.min())
    print("数组平均值：", arr1.mean())

    # 6. 切片取值
    print("数组前3个元素：", arr1[:3])
    print("二维数组第一行：", arr2[0])