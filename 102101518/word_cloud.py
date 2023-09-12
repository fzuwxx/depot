from wordcloud import WordCloud, ImageColorGenerator
import jieba
import pandas as pd
from PIL import Image
import numpy as np

'''词云图的制作'''


def citu():
    try:
        file_path = 'danmu_data.csv'
        # 读取 CSV 文件
        df = pd.read_csv(file_path)
        txt = ''.join(df.astype(str).values.flatten())
        txt_list = jieba.lcut(txt)
        string = ' '.join(txt_list)

        # 读取自定义的图片作为词云图背景
        mask_image = "Background2.jpg"
        mask = np.array(Image.open(mask_image))

        # 创建词云图对象，并设置参数
        wc = WordCloud(background_color='white',
                       font_path='C:/Windows/Fonts/SIMLI.TTF',
                       width=1000, height=700,
                       contour_width=5, contour_color='white',
                       mask=mask)

        # 生成词云图
        wc.generate(string)

        # # 根据图片颜色生成词云图的颜色
        # image_colors = ImageColorGenerator(mask)
        # wc.recolor(color_func=image_colors)

        # 保存词云图
        wc.to_file('wordcloud.png')

    except Exception as e:
        print("词云图制作报错：", e)
