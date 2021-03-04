import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

years = ['2019', '2020', '2021']
values = [100, 300, 600]
x = np.arange(len(years))

# bar차트 옵션
# width : 막대 너비 (default : 0.8)
# color : 막대 색상
# linewidth : 테두리 두께
# edgecolor : 테두리 색상
# align : tick 기준 막대 위치 조절 {'edge', 'center'} (default: center)
# tick_label : list 지정 시 순서대로 tick 표시
# log : y축 log scale로 표시

# 색상
color = ['red', 'yellow', 'blue']

bar_chart = plt.bar(x, values, width=0.4, color=color, linewidth=3, edgecolor="black", align='center', tick_label=years, log=True)

# 배경 색상 지정
plt.gca().set_facecolor('#E6F0F8')

# 축 색상 지정
plt.gca().spines['bottom'].set_color('red')

# 폰트 색상 지정
plt.xticks(color='#00517C', fontsize=10)

# 막대에 값 표기
for p in bar_chart.patches:
    left, bottom, width, height = p.get_bbox().bounds
    plt.annotate(f"{int(height)}", (left+width/2, height-8), ha='center', size=10, color='black')

# x축 tick
plt.xticks(x, years)
# y축 tick 제거
# plt.yticks(ticks= [])

# 테두리 제거
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.show()


