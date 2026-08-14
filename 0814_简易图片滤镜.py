# main.py 简易图片滤镜（PIL）
from PIL import Image

def grayscale_filter(img_path, save_path):
    img = Image.open(img_path)
    gray_img = img.convert("L")
    gray_img.save(save_path)
    print(f"灰度滤镜图片已保存至 {save_path}")

def flip_filter(img_path, save_path):
    img = Image.open(img_path)
    flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip_img.save(save_path)
    print(f"水平翻转图片已保存至 {save_path}")

if __name__ == "__main__":
    input_file = "test.jpg"
    grayscale_filter(input_file, "gray.jpg")
    flip_filter(input_file, "flip.jpg")