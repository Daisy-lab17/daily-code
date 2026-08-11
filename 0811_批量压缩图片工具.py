# 导入第三方图像处理库Pillow和系统文件模块
from PIL import Image
import os
from pathlib import Path

def compress_single_image(input_img_path: str, output_save_path: str, compress_quality=80, max_pixel=1920):
    """
    压缩单张图片
    :param input_img_path: 原图路径
    :param output_save_path: 压缩后保存路径
    :param compress_quality: 压缩画质 1~100，数字越小体积越小、画质越低
    :param max_pixel: 图片长边最大像素，超过自动等比例缩小
    """
    input_path = Path(input_img_path)
    output_path = Path(output_save_path)
    try:
        # 打开图片
        with Image.open(input_path) as img:
            # 透明通道图片转为RGB，避免JPG保存报错
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # 长边超过限制则等比例缩放
            if max(img.width, img.height) > max_pixel:
                img.thumbnail((max_pixel, max_pixel), Image.Resampling.LANCZOS)

            # 保存压缩后的图片，开启编码优化
            img.save(
                output_path.with_suffix(".jpg"),
                format="JPEG",
                quality=compress_quality,
                optimize=True
            )

            # 计算压缩节省空间比例
            original_size = os.path.getsize(input_img_path) / 1024
            new_size = os.path.getsize(output_path.with_suffix(".jpg")) / 1024
            save_percent = (1 - new_size / original_size) * 100
            print(f"✅ {input_path.name} | {original_size:.1f}KB → {new_size:.1f}KB，节省 {save_percent:.1f}%")

    except Exception as err:
        print(f"❌ 压缩失败 {input_path.name}：{str(err)}")

def batch_compress_folder(input_folder: str, output_folder: str):
    """批量压缩整个文件夹内所有图片"""
    support_suffix = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹所有文件
    for filename in os.listdir(input_folder):
        suffix = Path(filename).suffix.lower()
        if suffix in support_suffix:
            in_full = os.path.join(input_folder, filename)
            out_full = os.path.join(output_folder, filename)
            compress_single_image(in_full, out_full)

if __name__ == "__main__":
    # 直接修改这里的文件夹路径即可使用
    INPUT_DIR = "./origin_img"
    OUTPUT_DIR = "./compressed_img"
    batch_compress_folder(INPUT_DIR, OUTPUT_DIR)