import requests

def get_public_ip():
    """调用公开接口获取本机公网IP"""
    url = "https://httpbin.org/ip"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        ip_addr = data.get("origin", "获取失败")
        print(f"✅ 当前公网IP：{ip_addr}")
        return ip_addr
    except Exception as e:
        print(f"❌ 请求异常：{str(e)}")
        return None


if __name__ == "__main__":
    print("===== 网络请求示例程序 =====")
    get_public_ip()