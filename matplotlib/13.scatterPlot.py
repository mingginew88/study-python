
import matplotlib.pyplot as plt
import numpy as np

# Reproducible random state
# seed()에 들어갈 파라미터 : 0에서 4294967295 사이의 정수
np.random.seed(39680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
