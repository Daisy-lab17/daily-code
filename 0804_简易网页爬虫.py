# 导入第三方爬虫库
import requests
from bs4 import BeautifulSoup

def get_web_info(target_url):
    """
    爬取网页基础信息工具
    :param target_url: 目标网页地址
    """
    # 请求头，模拟浏览器访问，防止网站拦截爬虫
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        # 发送网络请求，设置10秒超时
        res = requests.get(url=target_url, headers=header, timeout=10)
        res.raise_for_status()  # 状态码非200直接抛出异常
        res.encoding = res.apparent_encoding  # 自动适配网页中文编码

        # 使用BeautifulSoup解析网页HTML代码
        soup = BeautifulSoup(res.text, "html.parser")

        # 1. 获取网页标题
        page_title = soup.find("title").text
        print("=" * 50)
        print(f"网页标题：{page_title}")
        print("=" * 50)

        # 2. 提取页面全部超链接
        all_links = soup.find_all("a")
        print(f"页面共找到 {len(all_links)} 个链接：")
        for index, a_tag in enumerate(all_links, start=1):
            link_text = a_tag.get_text(strip=True) or "无文字"
            link_href = a_tag.get("href")
            print(f"{index}. 文字：{link_text} | 地址：{link_href}")

        # 3. 将完整网页源码保存到本地html文件
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(res.text)
        print("\n✅ 网页源码已保存至 page_source.html")

    except requests.exceptions.RequestException as err:
        print(f"网络请求出错：{err}")


# 程序入口，运行爬虫
if __name__ == "__main__":
    # 测试网址：百度首页（稳定可爬取）
    test_url = "https://www.baidu.com"
    get_web_info(test_url)