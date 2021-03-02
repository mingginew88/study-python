import matplotlib.pyplot as plt


#################################################
# 그래프 옵션
# color, marker, linestyle 옵션 사용 가능
# color의 경우  Hex Code 및 색상 이름 사용

# 사용법 (색상 + 마커 + 라인) 순으로 plot() 옵션으로 입력
# 색상 종류 - b(blue), g(green), r(red), c(cyan), m(magenta), y(yello), w(white), k(black) ...
# 마커 종류 - o(circle), .(point), ,(pixel), v(triangle-down), ^(triangle-up), 1(tri-down), 2(tri-up), s(square), *(star), +(plus), D(diamond)
# 라인 종류 - -(solid line), --(dashed line), -.(dash-dot line), :(dotted line)
#################################################

plt.plot([1, 2, 3, 4], [2, 4, 7, 11], 'b^--')
plt.plot([1, 2, 3, 4], [1, 3, 5, 7], 'r+-.')
plt.plot([1, 2, 3, 4], [3, 4, 6, 8], color='violet')
plt.plot([1, 2, 3, 4], [9, 5, 2, 1], color='lawngreen')

# X축 명칭 표기
plt.xlabel('x-axis')
# Y축 명칭 표기
plt.ylabel('y-axis')

# 축 범위 지정 - 반드시 네 개의 값 (xmin, xmax, ymin, ymax)이 있어야 함.
plt.axis([0, 5, 0, 15])

# pyplot을 이용한 시각화
plt.show()
