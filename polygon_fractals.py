import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def next_point(u, v):
    j = np.random.randint(0, m)
    return alpha * u + (1 - alpha) * X[j], alpha * v + (1 - alpha) * Y[j]


def proportion(n):
    half = n // 2
    return np.sqrt((1 - np.cos(half * 2 * np.pi / n)) / (1 - np.cos(2 * np.pi / n)))


def alpha_calc(n):
    return 1 / (proportion(n) + 1)


# parameters:
m = 7  # number of sides
alpha = alpha_calc(m)  # next_point = alpha * prev_point + (1 - alpha) * vertex
# alpha = 0.33
N = 100000  # number of points
animation = False

fig = plt.figure(figsize=(7, 7))
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)

# polygon
X = np.cos(2 * np.pi * np.array(range(m)) / m)
Y = np.sin(2 * np.pi * np.array(range(m)) / m)

A = []
B = []
a, b = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
for _ in range(N):
    a, b = next_point(a, b)
    A.append(a)
    B.append(b)

if animation:
    graph, = plt.plot([], [], 'g.')

    def animate(i):
        graph.set_data(A[:i+1], B[:i+1])
        return graph

    plt.plot(X, Y, 'ro')
    ani = FuncAnimation(fig, animate, frames=N, interval=1)

else:
    plt.plot(X, Y, 'ro')
    plt.plot(A, B, 'g,')

print(f'alpha = {alpha}')
plt.show()
