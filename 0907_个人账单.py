# 简易个人记账本
import json
import os

# 保存记账数据的文件
DATA_FILE = "account.json"

def load_data():
    """读取本地记账文件，文件不存在则返回空列表"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(record_list):
    """把记账记录保存到json文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(record_list, f, ensure_ascii=False, indent=2)

def add_record(record_list):
    """新增一笔收支记录"""
    print("\n==== 添加记账记录 ====")
    item = input("输入用途（例如：午饭、奶茶）：")
    try:
        money = float(input("输入金额（支出填正数，收入填负数）："))
    except ValueError:
        print("金额输入错误！")
        return
    record = {
        "item": item,
        "money": money
    }
    record_list.append(record)
    save_data(record_list)
    print("✅ 添加成功")

def show_all(record_list):
    """展示全部账单，统计总支出"""
    print("\n==== 全部账单 ====")
    total = 0
    if len(record_list) == 0:
        print("暂无记账记录")
        return
    for idx, r in enumerate(record_list, start=1):
        print(f"{idx}. {r['item']}  {r['money']} 元")
        total += r["money"]
    print(f"\n📊 当前总支出：{total:.2f} 元")

def main():
    record_list = load_data()
    while True:
        print("\n===== 个人记账本 =====")
        print("1、新增一笔账单")
        print("2、查看全部账单")
        print("0、退出程序")
        op = input("请选择功能序号：")
        if op == "1":
            add_record(record_list)
        elif op == "2":
            show_all(record_list)
        elif op == "0":
            print("👋 退出记账程序，数据已保存")
            break
        else:
            print("输入无效，请重新选择")

if __name__ == "__main__":
    main()