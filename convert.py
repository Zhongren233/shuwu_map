import pandas as pd
import json

# 从JSON文件读取数据
json_file_path = 'store_data.json'
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理JSON数据
processed_data = []
for entry in data:
    # 提取经纬度
    longitude,latitude  = entry["location"].split(",")

    # 生成描述字段
    description = f"备注：{entry['notes']}，人均：{entry['amount']}，视频地址：{entry['video']}"

    # 构造新的行数据
    processed_data.append({
        "名称": entry["store_name"],
        "*经度": longitude.strip(),
        "*纬度": latitude.strip(),
        "*地址": entry["address"],
        "颜色": 1,  # 固定颜色为1
        "图标(外轮廓)": None,  # 留空
        "图标(填充物)": None,  # 留空
        "描述": description,
        "文件夹": None  # 留空
    })

# 将数据转换为pandas DataFrame
df = pd.DataFrame(processed_data)

# 确保列顺序与模板一致
columns_order = ['名称', '*经度', '*纬度', '*地址', '颜色', '图标(外轮廓)', '图标(填充物)', '描述', '文件夹']
df = df[columns_order]

# 导出为Excel文件
output_file = '处理后的数据.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='标记位置')

print(f"数据已成功处理并保存为 {output_file}")
