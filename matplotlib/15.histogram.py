import matplotlib.pyplot as plt
import numpy as np

# 45 - 100까지의 몸무게 중 10명의 랜덤 몸무게 리스트의 히스토그램.
n = 20

weight_list = [i for i in range(45, 100)]
weight = np.random.choice(weight_list, size=n)

plt.hist(weight, color='lightgreen')
plt.show()
