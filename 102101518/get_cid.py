import requests
import json

'''根据bvid请求得到cid'''


def get_cid(bvid):

    # 视频地址：https://www.bilibili.com/video/BV1PK4y1b7dt?t=1
    url = 'https://api.bilibili.com/x/player/pagelist?bvid='+str(bvid)+'&jsonp=jsonp'
    res = requests.get(url).text
    # 将获取的网页json编码字符串转换为python对象
    json_dict = json.loads(res)
    print(json_dict)
    return json_dict["data"][0]["cid"]
