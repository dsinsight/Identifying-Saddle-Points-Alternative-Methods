# Define the function f(x, y) = x^2 - y^2
def f(x, y):
    return x**2 - y**2

# Create grid points for x and y
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
x, y = np.meshgrid(x, y)
z = f(x, y)

# Plot the contour plot
plt.figure(figsize=(8, 6))
contour = plt.contour(x, y, z, levels=20, cmap='coolwarm')
plt.colorbar(contour)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Contour Plot: f(x, y) = x^2 - y^2')
plt.show()
