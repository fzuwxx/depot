import requests
import json

'''得到bvid'''


def get_bvid(page, pos):
    # 通过搜索api“https://api.bilibili.com/x/web-interface/search/all/v2?page=&keyword=”获取前300个视频的bvid，其中page为1-15，keyword为“日本核污染水排海”
    _url = 'https://api.bilibili.com/x/web-interface/search/all/v2?page='+str(page+1)+'&keyword=日本核污染水排海'
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
        'cookie': "buvid3=84494823-6825-4308-FB2B-6A7A8368B42566066infoc; b_nut=1684242766; CURRENT_FNVAL=4048; _uuid=21010568AE-754A-8159-C754-6D5C27F10107B866445infoc; buvid4=42FAC9B1-0422-0A2A-8A64-82F43936FFA871340-022022019-H0Dgo27GdvKzjHRGWFdXiw%3D%3D; buvid_fp=b5f7b890d23b3c02c06cc18eaa6417d3; rpdid=|(RYkm|~JJu0J'uY)RkRk~~|; i-wanna-go-back=-1; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; home_feed_column=5; DedeUserID=1460134606; DedeUserID__ckMd5=187e8dfdff780cc7; b_ut=5; nostalgia_conf=-1; CURRENT_QUALITY=64; PVID=1; browser_resolution=1488-742; SESSDATA=587edd32%2C1709184545%2Cd3355%2A913IpTnXrMod4HMCSeYYRaYLOo9QDYXObvfOLMTnd7StvuIEF-hseEzI4HHTs0WmbXVblGzgAABgA; bili_jct=9d23bd6f285f8004da547bbfbfa382f4"}
    res = requests.get(url=_url, headers=_headers, verify=False).text
    json_dict = json.loads(res)
    # print(json_dict)
    return json_dict["data"]["result"][11]["data"][pos]["bvid"]
