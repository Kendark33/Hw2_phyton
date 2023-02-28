# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Введите кол-во монет: '))
orel = 0
reshka = 0
random_list = [random.randint(0, 1) for i in range(len(n))]
print(random_list)
if random_list[i] == 0:
    orel += 1
else:
    reshka += 1
print(orel)
print(reshka)
# if reshka > orel:
#     print(orel)
# else:
#     print(reshka)
