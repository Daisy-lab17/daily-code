books = [
    {"name":"第七天","author":"余华"},
    {"name":"活着","author":"余华"},
    {"name":"三体","author":"刘慈欣"}
]

while True:
    print("\n====图书管理系统====")
    print("1.查看全部书籍")
    print("2.按书名搜索")
    print("3.添加新书")
    print("0.退出")
    op = int(input("请输入功能序号："))

    if op == 1:
        for b in books:
            print(f"《{b['name']}》 作者：{b['author']}")
    elif op == 2:
        key = input("输入要查找的书名：")
        find = False
        for b in books:
            if key in b["name"]:
                print(f"找到：《{b['name']}》 作者：{b['author']}")
                find = True
        if not find:
            print("没有这本书")
    elif op == 3:
        n = input("书名：")
        a = input("作者：")
        books.append({"name":n,"author":a})
        print("添加成功！")
    elif op == 0:
        print("程序结束")
        break
    else:
        print("输入无效")