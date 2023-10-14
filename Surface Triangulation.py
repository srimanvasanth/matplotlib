import numpy as np
import matplotlib.pyplot as plt

theta = 2*np.pi*np.random.random(1000)
r = 4*np.random.random(1000)
x = np.ravel(r*np.sin(theta))
y = np.ravel(r*np.cos(theta))

def f(x, y):
    return np.sin(np.sqrt(x**2+y**2))

z = f(x, y)
# fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_trisurf(x, y, z, cmap="viridis", edgecolor='none')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel('z')
plt.show()
