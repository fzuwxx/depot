import pandas as pd

'''输出数量前20弹幕'''


def print_danmu():
    try:
        # 读取 csv 文件，从第一列开始读取数据
        all_danmu = pd.read_csv('danmu_data.csv', header=None, encoding='utf-8')

        # 统计每个弹幕出现的次数
        counter = all_danmu.stack().value_counts()

        # 转换为 DataFrame 并重置索引
        top_20 = counter.head(20).reset_index()

        # 重命名列名
        top_20.columns = ['弹幕', '出现次数']

        print(top_20)
    except Exception as e:
        print("error:", e)
