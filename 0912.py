from PIL import Image

def create_check_mark():
    img = Image.new("RGB", (400, 200), color=(20, 30, 40))
    pixels = img.load()
    for x in range(50, 180):
        y = int(0.8 * x - 20)
        if 20 <= y <= 180:
            pixels[x, y] = (80, 200, 120)
    for x in range(140, 350):
        y = int(-0.6 * x + 215)
        if 20 <= y <= 180:
            pixels[x, y] = (80, 200, 120)
    img.save("check_in.png")
    print("✅ GitHub打卡图已生成 check_in.png")

if __name__ == "__main__":
    create_check_mark()