import numpy as np
import matplotlib.pyplot as plt

# Define the paths along x-axis and y-axis
x_path = np.linspace(-2, 2, 400)
y_path = np.linspace(-2, 2, 400)
f_x_path = x_path**2  # f(x, 0) = x^2
f_y_path = -y_path**2  # f(0, y) = -y^2

# Plot the paths
plt.figure(figsize=(8, 6))
plt.plot(x_path, f_x_path, label='f(x, 0) = x^2 (minimum)', color='blue')
plt.plot(y_path, f_y_path, label='f(0, y) = -y^2 (maximum)', color='red')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add labels and legend
plt.xlabel('X or Y')
plt.ylabel('f(x, y)')
plt.title('Path Behavior at Critical Point: Saddle Point Analysis')
plt.legend()
plt.show()
