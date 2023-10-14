import numpy as np
import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax = plt.axes(projection="3d")
# Data for 3D line
z = np.linspace(0,50,800)
x = np.sin(z)
y = np.cos(z)
ax.plot(x,y,z,"gray")
# or ax.plot3D(x,y,z,"gray")

# Data for scattered points
Z = 18*np.random.random(200)
X = np.sin(Z) + 0.1*np.random.random(200)
Y = np.cos(Z) + 0.1*np.random.random(200)
ax.scatter(X,Y,Z,c=Z,cmap="Greens")
# or ax.scatter3D(X,Y,Z,c=Z,cmap="Greens")
plt.show()
