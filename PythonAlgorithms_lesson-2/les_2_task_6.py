'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 2.
Задание # 6.

В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
'''

import random

n = random.randint(0, 100)
count = 1

print(f'Для удобства проверки задания вывожу загаданное число {n}')

for count in range(1, 11):
    attempt = int(input(f'Попытка {count}) Ваше предположение насчет загаданного числа:'))
    if attempt == n:
        break
    elif attempt > n:
        print('   Предложенный Вами вариант больше загаданного числа.')
    elif attempt < n:
        print('   Предложенный Вами вариант меньше загаданного числа.')

print(f'Вы молодец. Число {n} угадано успешно!' if attempt == n else f'Вы не угадали. Было загадано {n}')
