import math

def f(x):
    return math.log(x) + math.sin(x/4)

def bisect_with_localization(a, h, b_max, epsilon):
    b = a + h
    fa = f(a)
    fb = f(b)

    # Пошук ділянки локалізації
    while fa * fb > 0 and b <= b_max:
        a = b
        b = a + h
        fa = f(a)
        fb = f(b)

    # Якщо межа b перевищує b_max, то корінь на даному діапазоні не знайдений
    if b > b_max:
        return None

    # Ітераційний процес
    while abs(b - a) > epsilon:
        x = (b + a) / 2
        fx = f(x)

        if fx * fa > 0:
            a = x
            fa = fx
        else:
            b = x
            fb = fx

    return (a + b) / 2

# Задані параметри
a = 0.1
h = 0.1
b_max = 3
epsilon = 1e-6

root = bisect_with_localization(a, h, b_max, epsilon)
if root:
    print(f"Корінь рівняння на ділянці [{a}, {b_max}] дорівнює: {root}")
else:
    print(f"Корінь на ділянці [{a}, {b_max}] не знайдений.")

# Перевірка вірності роботи алгоритму
if abs(f(root)) < epsilon:
    print("Робота алгоритму вірна")
else:
    print("Робота алгоритму не вірна")