from datetime import datetime


def write_checkin():
    # 获取今天日期
    today = datetime.now().strftime("%Y‑%m‑%d")
    print(f"=== GitHub 打卡 {today} ===")

    trending = input("今日浏览Trending项目：")
    learn = input("今日学到：")
    commit = input("本地提交情况：")
    plan = input("明日计划：")

    # 拼接打卡内容
    content = f"""
## 📅 {today}
### 🔍 今日浏览Trending项目
- {trending}

### 💡 学习收获
- {learn}

### ✅ 本地仓库提交
- {commit}

### 🎯 明日计划
- {plan}
---
"""
    # 追加写入日志文件
    with open("checkin_log.md", "a", encoding="utf‑8") as f:
        f.write(content)

    print("\n✅打卡已保存到 checkin_log.md")


if __name__ == "__main__":
    write_checkin()