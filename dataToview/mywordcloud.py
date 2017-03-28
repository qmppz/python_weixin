# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from locale import *
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""
from os import path

import os
from scipy.misc import imread
import matplotlib.pyplot as plt
import locale
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

# 读取文本 alice.txt 在包文件的example目录下
#内容为
"""
Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org
"""
text = open(path.join(d, 'test.txt')).read()

# read the mask / color image
# taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
# 设置背景图片
alice_coloring = imread(path.join(d, "ico1.jpg"))


print locale.getdefaultlocale()    
#print "%s"%(locale.getlocale("LC_CTYPE"))
#locale.setlocale(locale.LC_ALL,"UTF-8")
locale.setlocale(locale.LC_ALL, 'chs')
#(locale.LC_ALL,locale.getdefaultlocale())

# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
#wc.generate(text)
frequencies = {'词a'.decode("utf-8"): 100,'词b'.decode("utf-8"): 90,'词c'.decode("utf-8"): 80}
#wordcloud = WordCloud().fit_words(frequencies)
wc = WordCloud(font_path = "H:/Python27/python_workplace/dataToview/font/msyh.ttc",
background_color="white", #背景颜色
max_words=2000,# 词云显示的最大词数
mask=alice_coloring,#设置背景图片
#stopwords=STOPWORDS.add("said"),
width=900,
height=600,
max_font_size=90, #字体最大值
random_state=42).fit_words(frequencies)

#wc.generate_from_frequencies(txt_freq)  
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(alice_coloring)

# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
# # 绘制词云
#plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
#plt.imshow(wc.recolor(color_func=image_colors))
#plt.axis("off")
# 绘制背景图片为颜色的图片
#plt.figure()
#plt.imshow(alice_coloring, cmap=plt.cm.gray)
# plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, "test1123.png"))