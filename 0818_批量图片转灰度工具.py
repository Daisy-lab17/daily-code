from PIL import Image
import os

def batch_to_grayscale(input_dir: str, output_dir: str):
    """
    将文件夹内所有图片批量转为灰度图
    :param input_dir: 原始图片文件夹路径
    :param output_dir: 输出灰度图保存路径
    """
    # 不存在输出文件夹就自动创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 支持的图片后缀
    suffix_list = (".jpg", ".jpeg", ".png", ".bmp")

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(suffix_list):
            input_path = os.path.join(input_dir, filename)
            try:
                img = Image.open(input_path)
                # convert('L') 转为8位灰度图
                gray_img = img.convert("L")
                out_path = os.path.join(output_dir, filename)
                gray_img.save(out_path)
                print(f"✅处理完成：{filename}")
            except Exception as e:
                print(f"❌处理失败 {filename}，错误：{e}")


if __name__ == "__main__":
    # 修改这里为你的文件夹路径
    INPUT_FOLDER = "./images"
    OUTPUT_FOLDER = "./gray_output"
    batch_to_grayscale(INPUT_FOLDER, OUTPUT_FOLDER)