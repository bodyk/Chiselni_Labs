import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Константи
U_max = 100  # Максимальна напруга в вольтах
f = 50  # Частота в Гц
R1, R2, R3, R4 = 5, 4, 7, 2  # Опори в омах
L1 = 0.01  # Індуктивність в генрі
C1, C2 = 300e-6, 150e-6  # Ємності в фарадах
time_end = 0.2  # Час закінчення симуляції в секундах
h = 0.00001  # Крок часу для неявного методу Ейлера в секундах

# Кількість кроків
steps = int(time_end / h)

# Масив часу
t = np.linspace(0, time_end, steps)

# Початкові умови
uc1 = 0  # Початкова напруга на конденсаторі C1
uc2 = 0  # Початкова напруга на конденсаторі C2

# Масиви для збереження результатів симуляції
uc1_values = np.zeros(steps)
uc2_values = np.zeros(steps)

# Функція для розрахунку вхідної напруги в залежності від часу
def U1(t):
    return U_max * np.sin(2 * np.pi * f * t)

# Функції рівнянь для неявного методу Ейлера
def equations(vars, t, uc1, uc2):
    uc1_next, uc2_next = vars
    u1 = U1(t)
    
    # Розрахунок струмів через резистори за законом Ома
    i_R1 = (u1 - uc1_next) / R1
    i_R3 = (uc1_next - uc2_next) / R3
    
    # Диференціальні рівняння
    duc1_dt = i_R1 / C1
    duc2_dt = i_R3 / C2
    
    # Рівняння для неявного методу Ейлера
    eq1 = uc1_next - uc1 - h * duc1_dt
    eq2 = uc2_next - uc2 - h * duc2_dt
    
    return [eq1, eq2]

# Цикл симуляції з використанням неявного методу Ейлера
for step in range(1, steps):
    # Використання fsolve для розв'язку системи рівнянь
    uc1_next, uc2_next = fsolve(equations, [uc1, uc2], args=(t[step], uc1, uc2))
    
    # Оновлення значень
    uc1, uc2 = uc1_next, uc2_next
    uc1_values[step] = uc1
    uc2_values[step] = uc2

# Побудова графіка вихідної напруги на конденсаторі C2
plt.plot(t, uc2_values)
plt.title('Вихідна напруга U2 на конденсаторі C2')
plt.xlabel('Час (с)')
plt.ylabel('Напруга (В)')
plt.grid(True)
plt.show()
