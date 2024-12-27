import requests
import json
import urllib.parse
import time

def get_amap_data(keywords: str):
    # 设置请求 URL 和必要的参数
    base_url = "https://lbs.amap.com/AMapService/v3/place/text"
    params = {
         # 你需要自己从浏览器里抓取请求，并补完params
        "keywords": urllib.parse.quote(keywords),
        "callback": f"jsonp_{int(time.time() * 1000)}"
    }

    # 设置请求头
    headers = {
        # 你需要自己从浏览器里抓取请求，并补完header
    }

    # 发送请求
    response = requests.get(base_url, headers=headers, params=params)

    # 处理响应数据
    if response.status_code == 200:
        # 返回的 JSONP 需要提取 JSON 内容
        jsonp_response = response.text
        json_data = jsonp_response[jsonp_response.index('(') + 1:jsonp_response.rindex(')')]
        data = json.loads(json_data)

        # 检查返回的 POI 数据
        if 'pois' in data and data['pois']:
            for poi in data['pois']:
                name = poi.get('name', '未知名称')
                location = poi.get('location', '未知位置')
                address = poi.get('address', '未知地址')
                tel = poi.get('tel', '暂无电话')

                # 输出信息
                print(f"名称: {name}")
                print(f"位置: {location}")
                print(f"address: {address}")
                print(f"电话: {tel}")
                print("-" * 30)
        else:
            print("没有找到相关数据.")
    else:
        print(f"请求失败，状态码: {response.status_code}")

def search_stores_in_json(json_file: str):
    # 读取 JSON 文件
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            store_data = json.load(f)

        # 遍历文件中的每个商店
        for store in store_data:
            address = store.get('store_name')
            if address:
                print(f"正在搜索名字：{address}")
                get_amap_data(address)
    except FileNotFoundError:
        print(f"文件 {json_file} 未找到。")
    except json.JSONDecodeError:
        print("文件格式错误，无法解析。")

# 示例用法：读取 store_data.json 文件
search_stores_in_json('store_data.json')
