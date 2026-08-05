# 导入第三方图像处理库 Pillow
from PIL import Image
import os
from pathlib import Path

class ImageTool:
    def __init__(self, input_dir="input_img", output_dir="output_img"):
        """初始化工具，自动创建输入输出文件夹"""
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        # 不存在则自动新建文件夹
        self.input_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
        # 支持的图片格式
        self.support_type = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]

    def get_image_info(self, img_path):
        """读取图片基础信息：尺寸、格式、色彩模式"""
        try:
            with Image.open(img_path) as img:
                info = {
                    "文件名": img_path.name,
                    "格式": img.format,
                    "宽高像素": img.size,
                    "色彩模式": img.mode
                }
                print(f"\n【图片信息】{info}")
                return info
        except Exception as e:
            print(f"读取图片信息失败：{e}")
            return None

    def compress_single_img(self, img_path, quality=70):
        """单张图片压缩，降低体积，保持画质"""
        try:
            with Image.open(img_path) as img:
                # png透明图不用转RGB，jpg必须转
                save_mode = img
                if img.format in ["JPEG", "JPG"]:
                    save_mode = img.convert("RGB")
                # 生成压缩后文件路径
                new_name = f"{img_path.stem}_压缩{img_path.suffix}"
                save_path = self.output_dir / new_name
                # 保存压缩图片
                save_mode.save(save_path, quality=quality, optimize=True)
                print(f"✅ 压缩完成：{save_path}")
                return save_path
        except Exception as e:
            print(f"❌ 压缩失败 {img_path.name}: {e}")

    def batch_convert_format(self, target_suffix=".jpg"):
        """批量转换图片格式，例如png全部转jpg"""
        all_img = [f for f in self.input_dir.iterdir() if f.suffix.lower() in self.support_type]
        if not all_img:
            print("输入文件夹无图片，请放入图片至input_img文件夹！")
            return
        for img_file in all_img:
            try:
                with Image.open(img_file) as img:
                    if target_suffix == ".jpg":
                        img = img.convert("RGB")
                    new_name = f"{img_file.stem}{target_suffix}"
                    save_path = self.output_dir / new_name
                    img.save(save_path, optimize=True)
                    print(f"格式转换：{img_file.name} → {new_name}")
            except Exception as e:
                print(f"转换失败 {img_file.name}: {e}")

    def batch_thumbnail(self, max_size=(500, 500)):
        """批量生成等比例缩略图，不拉伸变形"""
        all_img = [f for f in self.input_dir.iterdir() if f.suffix.lower() in self.support_type]
        if not all_img:
            print("输入文件夹无图片，请放入图片至input_img文件夹！")
            return
        for img_file in all_img:
            try:
                with Image.open(img_file) as img:
                    img.thumbnail(max_size)
                    new_name = f"{img_file.stem}_缩略图{img_file.suffix}"
                    save_path = self.output_dir / new_name
                    img.save(save_path)
                    print(f"缩略图生成：{new_name}")
            except Exception as e:
                print(f"缩略图失败 {img_file.name}: {e}")

# 程序入口
if __name__ == "__main__":
    tool = ImageTool()
    print("==== Python Pillow图片批量工具 ====")
    print("1. 查看单张图片信息")
    print("2. 批量压缩图片")
    print("3. 批量转换图片格式为JPG")
    print("4. 批量生成缩略图")
    choice = input("请输入功能序号：")

    if choice == "1":
        # 读取第一张图片信息
        img_list = list(tool.input_dir.glob("*"))
        if img_list:
            tool.get_image_info(img_list[0])
    elif choice == "2":
        tool.batch_convert_format()
    elif choice == "3":
        tool.batch_convert_format(target_suffix=".jpg")
    elif choice == "4":
        tool.batch_thumbnail()
    else:
        print("输入错误，程序退出")