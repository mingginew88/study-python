import matplotlib.pyplot as plt

# 그래프 영역 채우기
# fill_between()  - y축 기준으로 채우기
# fill_betweenx() - x축 기준으로 채우기
# fill() - 임의 범위 채우기

x = [1, 2, 3, 4, 5, 6]
y1 = [1, 4, 9, 16, 25, 36]
y2 = [1, 2, 4, 8, 10, 12]

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlabel('xLabel')
plt.ylabel('yLabel')

# y축 기준으로 채우기
plt.fill_between(x[2:4], y1[2:4], y2[2:4], color='#808000', alpha=0.5)
# x축 기준으로 채우기
plt.fill_betweenx(y1[4:6], x[4:6], color='#000080', alpha=0.5)
# 임의 범위 채우기
plt.fill([1.5, 2, 3.5, 4.0, 2.5], [4, 7, 11, 8, 5], color='#A4AAA7', alpha=0.5)

plt.show()