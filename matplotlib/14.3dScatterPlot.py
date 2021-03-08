import matplotlib.pyplot as plt
import numpy as np

def rand_range(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 50, 0, 50, 0, 50
cmin, cmax = 0, 2
xs = np.array([rand_range(n, xmin, xmax)])
ys = np.array([rand_range(n, ymin, ymax)])
zs = np.array([rand_range(n, zmin, zmax)])
color = np.array([rand_range(n, cmin, cmax)])

# fig 사이즈
plt.rcParams['figure.figsize'] = (4, 4)
fig = plt.figure()
# add_subplot(mno) mxn 그리드의 o번째에 그리기
ax = fig.add_subplot(221, projection='3d')
# cmap : [rainbow, Greens, Reds, Blues, autumn, RdYlGn] 등...
ax.scatter(xs, ys, zs, c=color, marker='o', s=15, cmap='rainbow')
plt.show()


## 이해가 안되는 점은 y축의 좌표 기준점이 왜 반대로 설정이 되는가...





