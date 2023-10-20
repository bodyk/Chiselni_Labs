import numpy as np


def gauss_elimination(A, b):
    """Розв'язок системи лінійних рівнянь методом Гаусса."""
    n = len(b)
    
    for i in range(n):
        # Вибір головного елементу по рядку
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        # Обернення рядків A[i]
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            b[j] -= factor * b[i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    # Знаходження розв'язку
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    return x


def system(x):
    """Визначення системи рівнянь."""
    x1, x2 = x
    f1 = (x1**2 - x2**2)**2 / 4 - x1**2 + x2**2 + 0.5 - x1
    f2 = x1 * x2 * (x1**2 - x2**2) + 0.5 - x2
    return np.array([f1, f2])


def jacobian(x):
    """Обчислення матриці Якобі для системи рівнянь."""
    x1, x2 = x
    return np.array([
        [2 * (x1**2 - x2**2) * x1 / 4 - 2 * x1 - 1, -2 * (x1**2 - x2**2) * x2 / 4 + 2 * x2],
        [x2 * (x1**2 - x2**2) + 2 * x1 * x2 * x1, x1 * (x1**2 - x2**2) - 2 * x1 * x2 * x2 - 1]
    ])


def newton_method(x0, eps):
    """Розв'язок системи рівнянь методом Ньютона."""
    x = x0
    while np.linalg.norm(system(x)) > eps:
        J = jacobian(x)
        F = system(x)
        delta = gauss_elimination(J, -F)
        x += delta
    return x


def is_solution_valid(x):
    """Перевірка коректності розв'язку."""
    return np.linalg.norm(system(x)) < 1e-5


def main():
    # Початкова точка наближення
    x0 = np.array([0.0, 0.0])
    # Відносна похибка
    epsilon = 1e-5
    # Знаходження розв'язку системи
    solution = newton_method(x0, epsilon)

    print("Solution:", solution)

    # Перевірка вірності розв'язку
    if is_solution_valid(solution):
        print("Розв'язок є правильним!")
    else:
        print("Розв'язок невірний.")


if __name__ == "__main__":
    main()
