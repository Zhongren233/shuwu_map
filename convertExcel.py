import pandas as pd

df = pd.read_excel('E:/树屋.xlsx', header=0)  # 第一行做列名
df.to_json('output.json', orient='records', force_ascii=False, indent=4)
