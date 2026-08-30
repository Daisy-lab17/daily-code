import requests
from bs4 import BeautifulSoup
import csv

def get_top250():
    headers = {
        "User‑Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    movies = []
    for start in range(0,250,25):
        url = f"https://movie.douban.com/top250?start={start}"
        resp = requests.get(url,headers=headers)
        soup = BeautifulSoup(resp.text,"html.parser")
        items = soup.find_all("div",class_="item")
        for item in items:
            title = item.find("span",class_="title").text
            score = item.find("span",class_="rating_num").text
            movies.append({"title":title,"score":score})
    #保存csv
    with open("douban_top250.csv","w",encoding="utf‑8‑sig",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["title","score"])
        writer.writeheader()
        writer.writerows(movies)
    print("爬取完成，已保存到 douban_top250.csv")

if __name__ == "__main__":
    get_top250()