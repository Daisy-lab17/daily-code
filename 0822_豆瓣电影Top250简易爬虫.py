import requests
from bs4 import BeautifulSoup
import csv
import time

# 请求头，模拟浏览器访问，防止被网站拦截
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def crawl_douban_movie():
    movie_list = []
    # 分页，每页25条数据，共10页
    for page in range(0, 250, 25):
        url = f"https://movie.douban.com/top250?start={page}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()  # 请求异常直接抛出错误
            soup = BeautifulSoup(resp.text, "lxml")
            items = soup.find_all("div", class_="item")

            for item in items:
                # 电影名称
                title = item.find("span", class_="title").get_text(strip=True)
                # 评分
                score = item.find("span", class_="rating_num").get_text(strip=True)
                # 评价人数
                people = item.find("div", class_="star").find_all("span")[-1].get_text(strip=True)
                # 简介
                quote_tag = item.find("span", class_="inq")
                quote = quote_tag.get_text(strip=True) if quote_tag else "无简介"

                movie_list.append({
                    "电影名称": title,
                    "评分": score,
                    "评价人数": people,
                    "短评": quote
                })
            print(f"已爬取第 {page//25 + 1} 页数据")
            time.sleep(1.5)  # 延时防封禁，合规爬虫
        except Exception as err:
            print(f"页面请求失败：{err}")
            break

    # 保存数据到csv文件
    with open("豆瓣Top250电影.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名称", "评分", "评价人数", "短评"])
        writer.writeheader()
        writer.writerows(movie_list)
    print(f"爬取完成，共获取 {len(movie_list)} 条电影数据，已保存至本地csv文件")

if __name__ == "__main__":
    crawl_douban_movie()