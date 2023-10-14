import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 15)
y = np.linspace(6, -6, 30)
X, Y = np.meshgrid(x, y)

def f(x, y):
    z = np.sin(np.sqrt(x**2 + y**2))
    return z

Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.contour3D(X,Y,Z,50,cmap="binary")
plt.show()
