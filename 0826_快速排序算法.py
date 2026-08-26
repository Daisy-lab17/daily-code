# main.py  快速排序算法演示（数据结构）
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_data = [22, 13, 5, 34, 8, 17, 1, 9]
    print("原始数组：", test_data)
    res = quick_sort(test_data)
    print("快排结果：", res)