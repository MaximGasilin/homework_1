'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 2.
Задание # 8.

Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
n = int(input('Введите количество чисел, в которых будем искать цифру: '))

target_digit = int(input('Введите цифру, которую будем искать в числах: '))
count_value = 0

print()

for count in range(1, n + 1):
    current_number = int(input('Очередное число, в которых будем искать цифру: '))
    if current_number == 0 and target_digit == 0:
        count_value += 1
    while current_number != 0:
        current_digit = current_number % 10
        current_number //= 10
        if target_digit == current_digit:
            count_value += 1

print(f'Цифра "{target_digit}" встречается {count_value} раз.')