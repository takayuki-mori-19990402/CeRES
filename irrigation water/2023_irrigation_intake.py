# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:06:39 2024

@author: HONGO-23
"""

# import library
import pandas as pd
from importlib import reload
import natsort 
reload(natsort)
import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# 対象期間の絞り込み（テストサイトの移植日は早くても-）
year =['2023/']
DOI= ['4/9','4/14',
      '4/19','4/24','4/29','5/4','5/9','5/14','5/19','5/24','5/29','6/3','6/8','6/13',
      '6/18','6/23','6/28','7/3','7/8','7/13','7/18','7/23','7/28','8/2','8/7','8/12','8/17',
      '8/22','8/27','9/1','9/6','9/11','9/16','9/21','9/26'] 
doi_date_2022 = [year[0] + d for d in DOI]

#栽培必要水量
umd_path = r"C:\Users\HONGO-23\Desktop\data\08_Irrigation\analysis\2023_water_intake.csv"
umd = pd.read_csv(umd_path)
fig, ax = plt.subplots()
umd.plot(ax=ax, figsize=(15,10), color=["b","g","purple"], marker="o", markersize=10, linewidth=6)
ax.set_ylabel("irrigation water intale (L/sec.)", fontsize=25)
ax.set_title("2023", fontsize=30)
day= DOI[0::5]
xax=list(range(0, 35, 5))
ax.set_xticks(xax)
ax.set_ylim(0,2500)
ax.set_xlim(0,30)
ax.set_xticklabels(day, rotation=45, fontsize = 100)
ax.tick_params(labelsize=30)
ax.grid()
ax.legend(fontsize=25)
#plt.savefig(r"C:\Users\HONGO-23\Desktop\data\ndvi_max day\fig\2023_water_intake.jpeg", dpi=200)