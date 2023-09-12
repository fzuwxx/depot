import requests
import re
import chardet

'''爬取弹幕'''


def get_data(cid):

    # https://api.bilibili.com/x/v1/dm/list.so?oid=XXX
    # 最终爬取API：https://api.bilibili.com/x/v1/dm/list.so?oid=?
    try:
        final_url = "https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid)
        final_res = requests.get(final_url)
        final_res.encoding = 'utf-8'
        final_res_encoding = chardet.detect(final_res.content)
        final_res = final_res.text
        pattern = re.compile('<d.*?>(.*?)</d>')
        data = pattern.findall(final_res)
        return data
    except Exception as e:
        print("执行get_data失败：", e)
