import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 待分析文本
text = """
人工智能是计算机科学的一个分支，它企图了解智能的实质，
并生产出一种新的能以人类智能相似的方式做出反应的智能机器，
该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。
人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大，
可以设想，未来人工智能带来的科技产品，将会是人类智慧的容器。
"""

# 中文分词
words = jieba.lcut(text)
processed_text = " ".join(words)

# 停用词，过滤无意义词汇
stop_words = {"的", "和", "是", "也", "该", "等", "从", "以来"}
word_list = processed_text.split()
word_list = [w for w in word_list if w not in stop_words]
final_text = " ".join(word_list)

# 创建词云对象
wc = WordCloud(
    font_path="C:/Windows/Fonts/simhei.ttf",  # 黑体，解决中文乱码
    width=1000,
    height=600,
    background_color="white",
    max_words=100,
    scale=2
)

wc.generate(final_text)

# 展示图片
plt.figure(figsize=(10, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# 保存词云图
wc.to_file("wordcloud.png")
print("词云图片已保存为 wordcloud.png")