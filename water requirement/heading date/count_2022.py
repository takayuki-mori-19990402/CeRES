# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:47:02 2024

@author: HONGO-23
"""

# settings
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルのパス
up_path = r"C:\Users\HONGO-23\Desktop\data\03_Shp\up.csv"
mid_path = r"C:\Users\HONGO-23\Desktop\data\03_Shp\mid.csv"
down_path = r"C:\Users\HONGO-23\Desktop\data\03_Shp\down.csv"
head_path = r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\csv\2022\2022_heading_date.csv" ## 変更

# データの読み込み
df_up = pd.read_csv(up_path)
df_mid = pd.read_csv(mid_path)
df_down = pd.read_csv(down_path)
df_head = pd.read_csv(head_path)

# 日付型に変換
df_head['Max_Date'] = pd.to_datetime(df_head['Max_Date'])

# 2021/4/14から2021/9/26までの日付を範囲としてカウント
date_range = pd.date_range(start='2022/3/30', end='2022/10/01', freq='D')                 ##変更
counts = df_head['Max_Date'].value_counts().reindex(date_range, fill_value=0)

# カウントが0以上の日付のみを取得
valid_dates = counts[counts > 3000]

# 'OBJECTID'列の一致をフィルタリング
common_up_ids = df_head[df_head['OBJECTID'].isin(df_up['UP'])]
common_mid_ids = df_head[df_head['OBJECTID'].isin(df_mid['MIDDLE'])]
common_down_ids = df_head[df_head['OBJECTID'].isin(df_down['DOWN'])]

# 一致した 'Max_Date' のみのカウントを取得
common_up_counts = common_up_ids['Max_Date'].value_counts().reindex(date_range, fill_value=0)
common_mid_counts = common_mid_ids['Max_Date'].value_counts().reindex(date_range, fill_value=0)
common_down_counts = common_down_ids['Max_Date'].value_counts().reindex(date_range, fill_value=0)

# マージしてインデックスが共通の日付だけを保持する
df_merge = pd.merge(valid_dates, common_up_counts, left_index=True, right_index=True, suffixes=('', '_up'))
df_merge = pd.merge(df_merge, common_mid_counts, left_index=True, right_index=True, suffixes=('', '_mid'))
df_merge = pd.merge(df_merge, common_down_counts, left_index=True, right_index=True, suffixes=('', '_down'))
df_merge = df_merge[["count_up"] + ["count_mid"] + ["count_down"]]
df_merge.index = df_merge.index.strftime('%m/%d')
df_merge = df_merge.T

# プロットの準備
fig, ax = plt.subplots(figsize=(10, 12))

# カスタムの色と凡例名を指定
colors = ['b', 'g', 'purple']  # 任意の色
labels = ['UP', 'MIDDLE', 'DOWN']  # 任意の凡例名

# 一致した部分の棒グラフをプロット
df_merge.T.plot(kind='bar', stacked=True, ax=ax, color=colors, width=0.6)

# 凡例の更新
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, labels, fontsize=25)

# プロットの詳細設定
plt.title('Counts of Paddy Field (>3000)', fontsize=35)
plt.xlabel('Heading Date', fontsize=35)
plt.ylabel('Count', fontsize=35)
plt.xticks(rotation=45)
plt.ylim(0, 40000)
plt.tick_params(labelsize=30)
plt.tight_layout()

# 横軸のラベルを取得
xticklabels = ax.get_xticklabels()

# 特定のラベルだけ赤くかつ太字にする
for label in xticklabels:
    if label.get_text() == '07/08':
        label.set_color('red')
        label.set_fontweight('bold')

# グラフの保存
plt.savefig(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\fig\2022_count_3000.jpeg", dpi=200)

# プロットを表示
plt.show()