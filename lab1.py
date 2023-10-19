import numpy as np

# Veriant 2
# s=0.02×2=0.04
# B=0.02×25=0.5

# Система рівнянь після підстановки:
# 8.3x1​+2.64x2​+4.1x3​+1.9x4​=−11.15
# 3.92x1+8.45x2+7.74x3+2.46x4=12.21
# 3.77x1+7.25x2+8.04x3+2.28x4=14.95
# 2.21x1+3.61x2+1.69x3+6.69x4=−8.35

# Матриця системи
A = np.array([
    [8.3, 2.64, 4.1, 1.9],
    [3.92, 8.45, 7.74, 2.46],
    [3.77, 7.25, 8.04, 2.28],
    [2.21, 3.61, 1.69, 6.69]
])

# Вектор вільних членів
b = np.array([-11.15, 12.21, 14.95, -8.35])

n = len(b)

# Прямий хід (з приведенням до верхньотрикутного вигляду)
for k in range(n-1):
    # Вибір головного елемента по стовпцю
    maxindex = abs(A[k:,k]).argmax() + k
    if A[maxindex, k] == 0:
        raise ValueError("Matrix is singular.")
    # Перестановка рядків
    if maxindex != k:
        A[[k,maxindex]] = A[[maxindex, k]]
        b[[k,maxindex]] = b[[maxindex, k]]
    for row in range(k+1, n):
        multiplier = A[row][k]/A[k][k]
        A[row][k:] = A[row][k:] - multiplier*A[k][k:]
        b[row] = b[row] - multiplier*b[k]

# Зворотний хід
x = np.zeros(n)
for k in range(n-1, -1, -1):
    x[k] = (b[k] - np.dot(A[k, k+1:], x[k+1:]))/A[k, k]

print(x)
