'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 2.
Задание # 9.

Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.вводом с клавиатуры.
'''
max_number = 0
max_summ = 0

entered_number = 1

print()

while entered_number != 0:
    entered_number = int(input('Введите натуральное число (для выхода введите "0"): '))

    if entered_number == 0:
        break

    current_number = entered_number
    current_summ = 0

    while current_number != 0:
        current_summ += current_number % 10
        current_number //= 10

    if current_summ > max_summ:
        max_summ = current_summ
        max_number = entered_number


print(f'Максимальная сумма цифр в числе "{max_number}". Сумма равна {max_summ}.')