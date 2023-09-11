'''将弹幕数据写入excel'''


def save_to_file(data):
    try:
        with open('danmu_data.xlsx', mode="a", encoding='utf-8') as f:
            for i in data:
                f.write(i)
                f.write("\n")
        f.close()
    except Exception as e:
        print("执行保存文件报错：", e)
