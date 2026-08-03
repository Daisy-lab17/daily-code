# 引入第三方库：PIL图像处理库、pytesseract文字识别库
from PIL import Image
import pytesseract

def image_to_text(img_path):
    """
    读取图片并提取图片内文字
    :param img_path: 图片文件路径
    :return: 识别出的文本字符串
    """
    try:
        # 打开图片文件
        img = Image.open(img_path)
        # 调用OCR识别图片文字，设置中英文识别
        text_result = pytesseract.image_to_string(img, lang='chi_sim+eng')
        return text_result
    except FileNotFoundError:
        return "错误：找不到对应图片文件，请检查路径"
    except Exception as err:
        return f"识别失败，报错信息：{err}"

def main():
    print("===== 图片OCR文字识别工具 =====")
    print("支持中文+英文图片文字提取")
    print("请将图片和代码放在同一文件夹，输入图片文件名即可")
    print("================================\n")
    file_name = input("输入图片名称（如 test.png）：")
    result = image_to_text(file_name)
    print("\n========= 识别结果 =========\n")
    print(result)

if __name__ == "__main__":
    main()