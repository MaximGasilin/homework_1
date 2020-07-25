'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 7.
Задание # 3.

Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

Формально сортировкой не пользовался, но поскольку этот метод разделяет список на основании операции больше или меньше,
то считаю, что это псевдосортировка. Тем не менее, более "не сортировочный" метод не нашел

'''
import random


def hoare_change_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return hoare_change(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (hoare_change(l, len(l) / 2 - 1, pivot_fn) +
                      hoare_change(l, len(l) / 2, pivot_fn))


def hoare_change(l, k, pivot_fn):
    if len(l) == 1:
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return hoare_change(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нашли медиану
        return pivots[0]
    else:
        return hoare_change(highs, k - len(lows) - len(pivots), pivot_fn)


n = 5
array = [random.randint(0, 99) for _ in range(2 * n + 1)]
print(array)
median_idx = hoare_change_median(array)
print(sorted(array))
print(median_idx)
