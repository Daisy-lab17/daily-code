import os

def batch_rename(folder_path: str, prefix: str):
    """
    批量重命名文件夹内所有文件
    :param folder_path: 目标文件夹路径
    :param prefix: 文件名统一前缀
    """
    if not os.path.isdir(folder_path):
        print("文件夹路径不存在")
        return

    files = os.listdir(folder_path)
    count = 1
    for name in files:
        old_full = os.path.join(folder_path, name)
        # 跳过子文件夹，只改文件
        if os.path.isdir(old_full):
            continue
        suffix = os.path.splitext(name)[1]
        new_name = f"{prefix}_{count}{suffix}"
        new_full = os.path.join(folder_path, new_name)
        os.rename(old_full, new_full)
        count += 1
    print(f"完成，共修改{count - 1}个文件")

if __name__ == "__main__":
    path = input("输入文件夹路径：")
    pre = input("输入文件名前缀：")
    batch_rename(path, pre)