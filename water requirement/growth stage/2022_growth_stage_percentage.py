# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:33:00 2024

@author: HONGO-23
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# 例としてデータフレームを作成
path_area = r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2022\20220723_growth_stage.csv"
df = pd.read_csv(path_area)
#print(df)


# 対象の成長値
growth_values = [3, 4, 5, 6, 7]

# growthの2,3,4,5,6,7に対応するareaの値の総和を計算
area_sums = {value: df[df['date'] == value]['area'].sum() for value in growth_values}

# 新しいデータフレームを作成
result_df = pd.DataFrame([area_sums])

# 列名を更新
result_df.columns = growth_values

print(result_df)
result_df.to_csv(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2022\20220723_growth_stage_percentage.csv")

# 総和を計算
total_area = sum(area_sums.values())

# 面積率を計算
area_percentages = {key: (value / total_area) * 100 for key, value in area_sums.items()}

# データフレームを作成し、面積率でソート
percent_df = pd.DataFrame(list(area_percentages.items()), columns=['date', 'Area Percentage'])
percent_df = percent_df.sort_values(by='Area Percentage', ascending=False).reset_index(drop=True)

# 積み上げ棒グラフを作成
colors = ['darkorchid', 'magenta', 'blue', 'orange', 'yellow']

plt.figure(figsize=(5, 70))

bottom = 0
for i, row in percent_df.iterrows():
    plt.bar(1, row['Area Percentage'], bottom=bottom, color=colors[i], edgecolor='black', label=f'Growth {row["date"]}')
    bottom += row['Area Percentage']

#plt.ylabel('%',fontsize=20)
#plt.title('Area Percentage', fontsize=40)
plt.xticks([])
plt.tick_params(labelsize=100)
plt.ylim(0, 100)
plt.gca().yaxis.set_major_formatter(PercentFormatter())
plt.savefig(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\fig\20220723_growth_percentage.jpeg", dpi=200, bbox_inches='tight')
plt.show()