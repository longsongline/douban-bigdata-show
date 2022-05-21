import csv

import jieba                            #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库
with open('dashuju.csv','r',encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[7] for row in reader]
print(column)
#分词
text = ""
for i in range(len(column)):
    text = text + column[i]
cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))


img = Image.open(r'D:\Install\big_screen-master (3)\big_screen-master\static\picture\map.png')   #打开遮罩图片
img_array = np.array(img)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)


#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴

# plt.show()    #显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'D:\shen.png',dpi=500)
# plt.savefig(r'.\static\assets\img\test.jpg',dpi=500)
