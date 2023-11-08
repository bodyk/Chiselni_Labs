import numpy as np

# Чисельне інтегрування за допомогою методу трапецій
def trapezoidal_rule(f, a, b, n):
    # Крок інтегрування
    h = (b - a) / n
    x = np.linspace(a, b, n+1)  # Точки розбиття
    fx = f(x)  # Значення функції в точках розбиття
    # Сума площ трапецій
    return h * (0.5 * fx[0] + 0.5 * fx[-1] + np.sum(fx[1:-1]))

# Визначення інтегруваної функції
def func(x):
    return 1 / (4 + x**2)

# Первісна функції
def antiderivative(x):
    return 0.5 * np.arctan(x / 2)

# Межі інтегрування та кількість трапецій
a, b, n = 0, 1, 1000

# Обчислення інтегралу методом трапецій
approx_integral = trapezoidal_rule(func, a, b, n)

# Точне значення інтегралу за формулою Ньютона-Лейбніца
exact_integral = antiderivative(b) - antiderivative(a)

# Виведення результатів
print(f'Наближене значення інтегралу: {approx_integral}')
print(f'Точне значення інтегралу: {exact_integral}')
print(f'Різниця: {abs(exact_integral - approx_integral)}')
