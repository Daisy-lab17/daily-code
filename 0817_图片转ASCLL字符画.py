from PIL import Image

# 灰度字符集，从暗到亮
ASCII_CHAR = r"@%#&*+=-:. "

def resize_img(image, new_width=100):
    """缩放图片，修正终端字符宽高比例"""
    w, h = image.size
    ratio = h / w / 1.65
    new_h = int(new_width * ratio)
    return image.resize((new_width, new_h))

def gray_img(image):
    """转为灰度图"""
    return image.convert("L")

def pixel_2_char(image):
    """像素映射成字符"""
    pixels = image.getdata()
    text = "".join([ASCII_CHAR[pix // 32] for pix in pixels])
    return text

def img_to_ascii(file_path, out_txt="output.txt", width=100):
    try:
        img = Image.open(file_path)
    except Exception as e:
        print(f"打开图片失败：{e}")
        return None

    img = resize_img(img, width)
    img = gray_img(img)
    ascii_text = pixel_2_char(img)

    # 按图片宽度换行
    lines = [ascii_text[i:i+width] for i in range(0, len(ascii_text), width)]
    final_text = "\n".join(lines)

    # 保存文本文件
    with open(out_txt, "w", encoding="utf‑8") as f:
        f.write(final_text)
    print(f"✅字符画已保存到 {out_txt}")
    return final_text


if __name__ == "__main__":
    # 修改这里为你的图片路径
    result = img_to_ascii("test.jpg", width=90)
    if result:
        print(result)