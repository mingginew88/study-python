import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 4, 7, 11])

# X축 명칭 표기
plt.xlabel('x-axis')
# Y축 명칭 표기
plt.ylabel('y-axis')

# 축 범위 지정 - 반드시 네 개의 값 (xmin, xmax, ymin, ymax)이 있어야 함.
plt.axis([0, 5, 0, 15])

# pyplot을 이용한 시각화
plt.show()
