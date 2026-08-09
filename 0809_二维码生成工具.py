# 导入第三方二维码库、图像处理库
import qrcode
from PIL import Image

def create_qrcode(content: str, save_name: str = "qrcode.png"):
    """
    生成二维码图片并保存到本地
    :param content: 二维码扫描后读取的内容（文字/网址）
    :param save_name: 生成的二维码保存文件名
    """
    # 初始化二维码配置
    qr = qrcode.QRCode(
        version=1,  # 二维码尺寸规格 1~40，数字越大可存储内容越多
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 容错率：中等
        box_size=10,  # 每个小格子像素大小
        border=2  # 二维码外边框宽度
    )
    # 写入需要编码的内容
    qr.add_data(content)
    qr.make(fit=True)

    # 自定义二维码颜色：黑色图案，白色背景
    img = qr.make_image(fill_color="black", back_color="white")
    # 保存图片
    img.save(save_name)
    print(f"二维码生成完成！保存文件名：{save_name}")

if __name__ == "__main__":
    # 示例：可以填网址、自我介绍、文本信息
    text = input("请输入二维码内容：")
    create_qrcode(text)