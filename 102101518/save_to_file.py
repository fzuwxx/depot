import csv

'''将数据写入csv'''


def save_to_file(data):
    try:
        with open('danmu_data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for d in data:
                writer.writerow([d])
        print("数据保存成功！")
    except Exception as e:
        print("执行保存文件报错：", e)
