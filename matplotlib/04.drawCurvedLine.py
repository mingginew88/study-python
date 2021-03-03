import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0, 4, 0.25)

# 여러 그래프 한줄 작성
# plt.plot(a, 10*a, 'r-', a, 2*a**2, 'ko', a, a**3, 'g-.')
# 각 그래프 그리기
# plt.plot(a, 10*a, 'r-')
# plt.plot(a, 2*a**2, 'ko')
# plt.plot(a, a**3, 'g-.')

# linewidth 및 markersize 설정
plt.plot(a, 10*a, 'r-', markersize=2)
plt.plot(a, 2*a**2, color='black', marker='*', linewidth=2)
plt.plot(a, a**3, color='green', marker='^', markersize=6)

plt.show()
