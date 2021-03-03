import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0, 3, 0.25)

# linewidth 및 markersize 설정
plt.plot(a, 10*a, 'r-', markersize=2)
plt.plot(a, 2*a**2, color='black', marker='*', linewidth=2)
plt.plot(a, a**3, color='green', marker='^', markersize=6)

# 그리드 설정
# plt.grid(True)

# 축 지정 axis = {‘both’, ‘x’, ‘y’} 에서 선택 가능 (default : both)
# plt.grid(True, axis='y')

# 그리드 옵션
# color, alpha, linestyle, which 등 옵션 변경 가능 (which : 'major', 'minor', 'both' 에서 선택 가능)
plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='-', which='major')

# 틱 설정 - 그래프의 축 간격을 구분하고자 표시하는 눈금
# xticks(), yticks(), tick_params()
plt.xticks(np.arange(0, 3, 0.25), labels=['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.yticks(np.arange(0, 40, 10), ('0', '1GB', '2GB', '3GB'))

# 틱 옵션 설정
# direction = {'in', 'out', 'inout'} 에서 선택 가능 눈금 안/밖
# length :눈금 길이
# width : 눈금 너비
# color : 눈금 색상
# pad : 눈금과 레이블 간의 거리
# labelsize : 레이블 크기
# labelcolor : 레이블 색상
# top/bottom/left/right : {True, False} 중 선택하여 눈금 위치 지정

plt.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=10, labelcolor='green', top=True)
plt.tick_params(axis='y', direction='inout', length=2, width=2, color='r', pad=3, labelsize=10, right=True)

plt.show()