import numpy as np
import matplotlib.pyplot as plt

# Define your ID function
def ID(x):
    return x**4 - 4*x**2 + 1

# Surface plots with different views
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
Z = ID(X)
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Surface Plot - View 1')

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.view_init(elev=30, azim=-60)
ax2.set_title('Surface Plot - View 2')

ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, Z, cmap='viridis')
ax3.view_init(elev=60, azim=-30)
ax3.set_title('Surface Plot - View 3')

plt.tight_layout()
plt.show()

# Contour plots with different windows
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
Z = ID(X)

ax1 = axes[0, 0]
ax1.contour(X, Y, Z, levels=20, cmap='viridis')
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_title('Contour Plot - Window 1')

ax2 = axes[0, 1]
ax2.contour(X, Y, Z, levels=20, cmap='viridis')
ax2.set_xlim(-1, 1)
ax2.set_ylim(-1, 1)
ax2.set_title('Contour Plot - Window 2')

ax3 = axes[1, 0]
ax3.contour(X, Y, Z, levels=20, cmap='viridis')
ax3.set_xlim(-0.5, 0.5)
ax3.set_ylim(-0.5, 0.5)
ax3.set_title('Contour Plot - Window 3')

ax4 = axes[1, 1]
ax4.contour(X, Y, Z, levels=20, cmap='viridis')
ax4.set_xlim(-0.1, 0.1)
ax4.set_ylim(-0.1, 0.1)
ax4.set_title('Contour Plot - Window 4')

plt.tight_layout()
plt.show()