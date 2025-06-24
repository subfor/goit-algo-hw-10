import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))

# Аналітичне обчислення інтеграла
result, error = spi.quad(f, a, b)

# Метод Монте-Карло
N = 10000
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)
under_curve = y_rand <= f(x_rand)
monte_carlo_area = (b - a) * f(b) * np.sum(under_curve) / N
# Випадкові точки
ax.scatter(
    x_rand[under_curve], y_rand[under_curve], color="green", s=1, label="Під кривою"
)
ax.scatter(
    x_rand[~under_curve], y_rand[~under_curve], color="blue", s=1, label="Над кривою"
)

explanation = f"Площа (quad): {result:.4f}\nПлоща (Monte-Carlo):{monte_carlo_area}"
ax.text(
    0.5,
    5.0,
    explanation,
    fontsize=10,
    bbox=dict(facecolor="white", alpha=0.8, boxstyle="round,pad=0.5"),
)
plt.grid()
plt.show()
