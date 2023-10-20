import numpy as np

# Вхідні дані
k = 2
p = 25
s = 0.02 * k
B = 0.02 * p

A_original = np.array([
    [8.3, 2.6 + s, 4.1, 1.9],
    [3.92, 8.45, 7.78 - s, 2.46],
    [3.77, 7.21 + s, 8.04, 2.28],
    [2.21, 3.65 - s, 1.69, 6.69]
])
A = A_original.copy()
b = np.array([-10.65 + B, 12.21, 15.45 - B, -8.35])

# 1. Прямий хід методу
n = A.shape[0]
for k in range(n):
    # Вибір головного елемента по стовпцю
    max_el = abs(A[k][k])
    max_row = k
    for i in range(k+1, n):
        if abs(A[i][k]) > max_el:
            max_el = abs(A[i][k])
            max_row = i
            
    # Перестановка рядків
    A[[k, max_row]] = A[[max_row, k]]
    b[k], b[max_row] = b[max_row], b[k]
    
    # Зведення до верхньої трикутної форми
    for i in range(k+1, n):
        factor = A[i][k] / A[k][k]
        for j in range(k, n):
            A[i][j] -= factor * A[k][j]
        b[i] -= factor * b[k]
        
# 2. Обернений хід
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = b[i]
    for j in range(i+1, n):
        x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]

print("Розв'язок системи: ", x)
print("Перевірка (Ax): ", np.dot(A_original, x))
print("Вектор вільних членів b: ", b)
