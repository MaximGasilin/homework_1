'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 7.
Задание # 2.

Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

Неоценимая помощь в описании алгоритма здесь: https://dev-gang.ru/article/slijanie-sortirovki-v-python-tfbgkwagro/

Реализовано 2 варианта
1. Рекурсивное классическое слияние
2. Без использования регкурсии. Основан на предположении, что в исходном массиве итак есть отсортированные куски.
   Просто находим их и "слияем".
'''

from random import randint


# Классическое рекурсивное слияние. Так называемое "сверху-вниз"
def merge_sort_down(array, left_index=None, right_index=None):
    if left_index is None:
        left_index = 0

    if right_index is None:
        right_index = len(array) - 1

    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort_down(array, left_index, middle)
    merge_sort_down(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


# Безрекурсивное слияние. Так называемое "снизу-вверх". Основано на том факте, что отдельные куски массива
# могут быть уже отсортированы. Поэтому, начиная с первого начинаем присоединять вышеупомянуты куски.
def merge_sort_up(array):
    left_index = 0
    middle = 0

    count = 1
    while count <= len(array)-1:
        if array[count-1] > array[count]:
            if middle != 0: # Выделение первой части для присоединения. Остальные будут с ней сливаться
                right_index = count-1
                merge(array, left_index, right_index, middle)
            middle = count - 1
        count += 1
    if count != right_index:
        right_index = count
        merge(array, left_index, right_index, middle)


# Базовая функция слияния двух подмассивов в один
def merge(array, left_index, right_index, middle):
    # Сделайте копии обоих массивов, которые мы пытаемся объединить

    # Увеличиваем второй параметр на 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle + 1:right_index + 1]

    # Начальные значения для переменных, которые мы используем для хранения
    # Курсор того, где мы находимся в каждом массиве
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Пройдите обе копии, пока у нас не закончатся элементы
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    # У нас закончились элементы в left_copy или right_copy
    # так что мы пройдемся по оставшимся элементам и добавим их
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

n = 10
array = [randint(0, 49) for _ in range(n)]
print('Исходный массив:        ', array)
if randint(0, 1):
    # 1. Рекурсивное классическое слияние
    merge_sort_down(array)
    print('Использован метод классического рекурсивного слияния.')
else:
    # 2. Без использования рекурсии.
    print('Использован метод без использования рекурсии.')
    merge_sort_up(array)
print('Отсортированный массив: ', array)
