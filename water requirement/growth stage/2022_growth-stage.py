# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:39:39 2024

@author: HONGO-23
"""

# import library
import pandas as pd
from importlib import reload
import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# 対象期間の絞り込み（テストサイトの移植日は早くても2021/4/15）
year =['2022/']
DOI = ['3/30','4/4','4/9','4/14','4/19','4/24','4/29','5/4','5/9','5/14',
       '5/19','5/24','5/29','6/3','6/8','6/13','6/18','6/23','6/28','7/3',
       '7/8','7/13','7/18','7/23','7/28','8/2','8/7','8/12','8/17', '8/22',
       '8/27','9/1', '9/6','9/11','9/16','9/21','9/26','10/1']
doi_date_2022 = [year[0] + d for d in DOI]


# 既存のCSVファイルを読み込む
input_file_path = r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2022\2022_heading_date.csv"
output_file_path = r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2022\2022_ndvi_max_date_updated.csv"

with open(input_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# ヘッダーリストを作成し、初期化
min_length = max(len(data[0]), len(doi_date_2022) + 2)
header = [""] * min_length

# 0列目と1列目にヘッダーを書き込む
header[0] = "OBJECTID"
header[1] = "max date"

# 2列飛ばしてヘッダーを書き込む
for i, value in enumerate(doi_date_2022):
    header[i + 2] = value

# ヘッダーをデータに反映
data[0] = header

# 修正したデータを新しいCSVファイルに書き込む
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

#日付けだけのファイルを読み込む
df_m = pd.read_csv(output_file_path)
df_m
#df_m.to_csv(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2021\2021_timeseries_nodate.csv")

# 日付差分を計算する関数を定義
def calculate_date_difference(date1_str, date2_str):
    date_format = "%Y/%m/%d"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    return (date2 - date1).days

for col in doi_date_2022:
    df_m[col] = df_m['max date'].apply(lambda x: calculate_date_difference(x, col))

# 出穂日からの経過日数だけのデータフレームに整序
df_dif = df_m[doi_date_2022]
#df_dif.to_csv(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2021\2021_dif_from_heading_date.csv")

#生育ステージ分類定義式
def growth_classify(n):
    n = int(n)
    if 56 <= n:
        return 9
    elif  41 <= n <=  55:
        return 8
    elif  21 <= n <=  40:
        return 7
    elif   1 <= n <=  20:
        return 6
    elif -19 <= n <=   0:
        return 5
    elif -54 <= n <= -20:
        return 4
    elif -74 <= n <= -55:
        return 3
    elif -84 <= n <= -75:
        return 2
    elif n <= -85:
        return 1
 
df_growth_stage = df_dif.applymap(growth_classify)
df_growth_stage.to_csv(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2022\2022_growth_stage.csv")
    
    
    
    
    
    
    
    