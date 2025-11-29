"""
Задача 1. Исполнитель «Плюс»
Исполнитель может выполнять команды: +1, +2 и +4.
Начальное число: 20. Конечное число: 30.
Требуется определить количество различных программ, приводящих число 20 к числу 30.
Ответ: одно число.

ПРОГРАММА ДОЛЖНА ПЕЧАТАТЬ НА ЭКРАНЕ ТОЛЬКО ОДНО ЧИСЛО (ОТВЕТ) И НИЧЕГО БОЛЬШЕ.
"""

# Решение будет здесь
import math

m = 0
n = 0
k = 0
solutions = []
sum = 0

for m in range(20):
    for n in range(20):
        for k in range(20):
            if m + 2 * n + 4 * k + 20 == 30:
                solutions.append([m, n, k])
                sum += math.factorial(m + n + k) / (math.factorial(m) * math.factorial(n) * math.factorial(k))

print(int(sum))