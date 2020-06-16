'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 5.
Задание # 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.

Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

Пояснения для проверяющих:
1. Вместо списка решил использовать deque из модуля collections. Т.к. решил,
что задача должна быть хоть как-то связана с темой урока.
2. Не вижу особой сложности сделать процедуры, которые работают не только для шестнадцатиричной, но и для любой другой.
Реализовал вплоть до 36-ричной. Для проверки монжо выбрать в качестве первого параметра
во всех функциях - систему счисления.
Но на вход им нужно подавать deque состоящие только из знаков принятых в этой системе.

Например:

addin_of_two_numbers(16, a, b) - складывает в 16-ричой системе
addin_of_two_numbers(32, a, b) - складывает в 32-ричой системе
multiply_of_two_numbers(16, n1, n2) - умножает в 16-ричой системе
multiply_of_two_numbers(2, n1, n2) - умножает в 2-ой системе

3. Основными функциями алгоритма являются addin_of_two_numbers и multiply_of_two_numbers. Но для их работы нужны
еще 2 функции:
__simple_addin_of_two_numbers - складывает 3 цифры (не числа)
__simple_multiply_of_two_numbers - умножает друг на друга 2 цифры (не числа) и прибавляет к ним еще одну цифру.
Это необходимо для имитации сложения столбиком и умножения столбиком. Помните фразу: "3 пишем, 2 в уме"?
Это ее реализация.

'''
from collections import deque

UNIVERSAL_NUMBER_BASE = '0123456789ABCDEFGHIJKLMNOPQASTUVWXYZ'


def __simple_addin_of_two_numbers(num_system, s1, s2, s3='0'):

    is1 = UNIVERSAL_NUMBER_BASE.index(s1)
    is2 = UNIVERSAL_NUMBER_BASE.index(s2)
    is3 = UNIVERSAL_NUMBER_BASE.index(s3)

    ires = is1 + is2 + is3
    ed = ires % num_system
    dec = ires // num_system

    result = str(dec) + UNIVERSAL_NUMBER_BASE[ed]

    return result


def __simple_multiply_of_two_numbers(num_system, s1, s2, s3='0'):

    is1 = UNIVERSAL_NUMBER_BASE.index(s1)
    is2 = UNIVERSAL_NUMBER_BASE.index(s2)
    is3 = UNIVERSAL_NUMBER_BASE.index(s3)

    ires = is1 * is2 + is3
    ed = ires % num_system
    dec = ires // num_system

    result = str(dec) + UNIVERSAL_NUMBER_BASE[ed]

    return result


def addin_of_two_numbers(num_system, n1, n2):

    result = deque()
    len_1, len_2 = len(n1), len(n2)

    memory_digit = '0'
    for count in range(0, max(len_1, len_2)):
        local_res = __simple_addin_of_two_numbers(num_system,
                                                  n1[len_1 - count - 1] if len_1 > count else '0',
                                                  n2[len_2 - count - 1] if len_2 > count else '0',
                                                  memory_digit)
        result.appendleft(local_res[1])
        memory_digit = local_res[0]

    if memory_digit != '0':
        result.appendleft(memory_digit)

    return result


def multiply_of_two_numbers(num_system, n1, n2):

    result = deque()
    len_1, len_2 = len(n1), len(n2)

    for count1 in range(0, len_1):
        interim = deque(('0 ' * count1).split() if count1 > 0 else [])
        memory_digit = '0'
        for count2 in range(0, len_2):
            local_res = __simple_multiply_of_two_numbers(num_system,
                                                         n1[len_1 - count1 - 1],
                                                         n2[len_2 - count2 - 1],
                                                         memory_digit)
            interim.appendleft(local_res[1])
            memory_digit = local_res[0]

        if memory_digit != '0':
            interim.appendleft(memory_digit)

        result = addin_of_two_numbers(num_system, result, interim)

    return result


if __name__ == '__main__':

    # Код для проверки примера из задания
    # a = deque('c4f'.upper())
    # b = deque('a2'.upper())
    # c = addin_of_two_numbers(16, a, b)
    # print(f'{a} + {b} = {c}')
    # d = multiply_of_two_numbers(16, a, b)
    # print(f'{a} * {b} = {d}')
    # print('-' * 10)
    # print(hex(15 + 16*4 + 16*16*12), ' + ',  hex(2 + 16*10), ' = ', hex((15 + 16*4 + 16*16*12) + (2 + 16*10)))
    # print(hex(15 + 16*4 + 16*16*12), ' * ',  hex(2 + 16*10), ' = ', hex((15 + 16*4 + 16*16*12) * (2 + 16*10)))

    a = deque(input('Введите пожалуйста первое число (a): ').upper())
    b = deque(input('Введите пожалуйста первое число (b): ').upper())
    c = addin_of_two_numbers(16, a, b)
    print(f'{a} + {b} = {c}')
    d = multiply_of_two_numbers(16, a, b)
    print(f'{a} * {b} = {d}')
