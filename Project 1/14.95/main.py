import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.polys.benchmarks.bench_solvers import x0

# Define the ID function
x, y = sp.symbols('x y')
f = x**4 - 4*x**2 + 1

# Task 1: Verify partial derivatives of Q
a, b = sp.symbols('a b')
Q = f.series(x, a, 2).removeO()
Q_first_derivative = Q.diff(x).subs(x, a).subs(y, b)
Q_second_derivative = Q.diff(x, 2).subs(x, a).subs(y, b)
print(f"First derivative of Q at (a, b): {Q_first_derivative}")
print(f"Second derivative of Q at (a, b): {Q_second_derivative}")
print()

# Task 2: Find Taylor polynomials L and Q
C = (x0, y0)  # Critical point obtained from Problem 14.94
L = f.series(x, C[0], 1).removeO() + f.series(y, C[1], 1).removeO()
Q = f.series(x, C[0], 2).removeO() + f.series(y, C[1], 2).removeO()

# Task 3: Compare values of f, L, and Q at (x0 + 0.1, y0 - 0.1)
values = {x: x0 + 0.1, y: y0 - 0.1}
f_value = f.subs(values)
L_value = L.subs(values)
Q_value = Q.subs(values)
print(f"f({values[x]}, {values[y]}) = {f_value}")
print(f"L({values[x]}, {values[y]}) = {L_value}")
print(f"Q({values[x]}, {values[y]}) = {Q_value}")
print()

# Task 4: Plot f, L, and Q
x_range = np.linspace(-2, 2, 200)
y_range = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x_range, y_range)
F = sp.lambdify((x, y), f)
L_func = sp.lambdify((x, y), L)
Q_func = sp.lambdify((x, y), Q)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, F(X, Y), alpha=0.5, cmap='viridis', label='f')
ax.plot_surface(X, Y, L_func(X, Y), alpha=0.5, cmap='plasma', label='L')
ax.plot_surface(X, Y, Q_func(X, Y), alpha=0.5, cmap='inferno', label='Q')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Comparison of f, L, and Q')
ax.legend()

plt.show()
