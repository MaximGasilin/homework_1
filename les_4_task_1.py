'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 4.
Задание # 1.

Для задания использовал задачу № 9 из 3-го урока:
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Комментарий из видео:
Найти минимальный элемент в каждом из столбцов, а потом среди этих минимальных найти максимальный.

 Вывод:
 1-й метод имеет эмпирическую оценку O(n**2)
 2-й и 3-й методы скорее O(n)
 Причем, 3-й метод максимально использует встроенные функции min, ma, map и показывает лучший результат.

 Для учета чистого времени прцедры поиска из основного времени было вычтено время генерации матрицы случайных чисел. Отраженное в 1-й секции.

Более подробно можно посмотреть страницу "Решето" в прикрепленном к задаче эксельном файле.
Файл не содерижт макросов или вирусов.

'''

from random import randint
import cProfile

def generate_matrix(n):
    matrix = []
    for i in range(0, n):
        matrix.append([0] * n)
        for j in range(0, n):
            matrix[i][j] = randint(1, 100)
    return matrix

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.generate_matrix(100)"
# 100 loops, best of 3: 7.04 msec per loop
# cProfile.run("generate_matrix(100)")
# 53084 function calls in 0.017 seconds

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.generate_matrix(200)"
# 100 loops, best of 3: 28.4 msec per loop
# cProfile.run("generate_matrix(200)")
# 211682 function calls in 0.069 seconds

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.generate_matrix(300)"
# 100 loops, best of 3: 66.2 msec per loop
# cProfile.run("generate_matrix(300)")
# 475731 function calls in 0.156 seconds

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.generate_matrix(400)"
# 100 loops, best of 3: 113 msec per loop
# cProfile.run("generate_matrix(400)")
# 845430 function calls in 0.276 seconds

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.generate_matrix(500)"
# 100 loops, best of 3: 177 msec per loop
# cProfile.run("generate_matrix(500)")
# 1320418 function calls in 0.424 seconds

def find_maximin_1(n):

    matrix = generate_matrix(n)

    maximin = 0
    for i in range(0, n):
        current_min = matrix[0][i]
        for j in range(0, n):
            if matrix[j][i] < current_min:
                current_min = matrix[j][i]
        if maximin < current_min:
            maximin = current_min
    return maximin

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_1(100)"
# 100 loops, best of 3: 8.13 msec per loop
# cProfile.run("find_maximin_1(100)")
# 52823 function calls in 0.395 seconds
# 1    0.097    0.097    0.394    0.394 les_4_task_1.py:27(find_maximin_1)
# 1    0.091    0.091    0.298    0.298 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_1(200)"
# 100 loops, best of 3: 32.7 msec per loop
# cProfile.run("find_maximin_1(200)")
# 211630 function calls in 1.500 seconds
# 1    0.099    0.099    1.500    1.500 les_4_task_1.py:27(find_maximin_1)
# 1    0.203    0.203    1.401    1.401 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_1(300)"
# 100 loops, best of 3: 80.8 msec per loop
# cProfile.run("find_maximin_1(300)")
# 475022 function calls in 4.103 seconds
# 1    0.103    0.103    4.102    4.102 les_4_task_1.py:27(find_maximin_1)
# 1    0.843    0.843    3.999    3.999 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_1(400)"
# 100 loops, best of 3: 134 msec per loop
# cProfile.run("find_maximin_1(400)")
# 845660 function calls in 6.398 seconds
# 1    0.297    0.297    6.398    6.398 les_4_task_1.py:27(find_maximin_1)
# 1    0.614    0.614    6.100    6.100 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_1(500)"
# 100 loops, best of 3: 214 msec per loop
# cProfile.run("find_maximin_1(500)")
# 1320851 function calls in 10.101 seconds
# 1    0.403    0.403   10.100   10.100 les_4_task_1.py:27(find_maximin_1)
# 1    1.213    1.213    9.697    9.697 les_4_task_1.py:4(generate_matrix)

def find_maximin_2(n):

    matrix = generate_matrix(n)

    maximin = 0
    for i in range(0, n):
        current_min = min(matrix[i])
        if maximin < current_min:
            maximin = current_min

    return maximin

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_2(100)"
# 100 loops, best of 5: 7.18 msec per loop
# 52997 function calls in 0.494 seconds
# 1    0.198    0.198    0.493    0.493 les_4_task_1.py:4(generate_matrix)
# 1    0.000    0.000    0.493    0.493 les_4_task_1.py:86(find_maximin_2)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_2(200)"
# 100 loops, best of 5: 29.1 msec per loop
# 211649 function calls in 2.301 seconds
# 1    0.491    0.491    2.299    2.299 les_4_task_1.py:4(generate_matrix)
# 1    0.000    0.000    2.301    2.301 les_4_task_1.py:86(find_maximin_2)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_2(300)"
# 100 loops, best of 5: 67.9 msec per loop
# 475655 function calls in 6.998 seconds
# 1    2.889    2.889    6.994    6.994 les_4_task_1.py:4(generate_matrix)
# 1    0.000    0.000    6.998    6.998 les_4_task_1.py:86(find_maximin_2)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_2(400)"
# 100 loops, best of 5: 115 msec per loop
# 845106 function calls in 9.694 seconds
# 1    2.169    2.169    9.684    9.684 les_4_task_1.py:4(generate_matrix)
# 1    0.000    0.000    9.693    9.693 les_4_task_1.py:86(find_maximin_2)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_2(500)"
# 100 loops, best of 5: 183 msec per loop
# 1321215 function calls in 18.601 seconds
# 1    5.279    5.279   18.398   18.398 les_4_task_1.py:4(generate_matrix)
# 1    0.000    0.000   18.504   18.504 les_4_task_1.py:86(find_maximin_2)

def find_maximin_3(n):
	matrix = generate_matrix(n)
	maximin = max(map(min, matrix))
	return maximin

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_3(100)"
# 100 loops, best of 5: 7.31 msec per loop
# 52926 function calls in 0.702 seconds
# 1    0.000    0.000    0.702    0.702 les_4_task_1.py:128(find_maximin_3)
# 1    0.102    0.102    0.606    0.606 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_3(200)"
# 100 loops, best of 5: 29.1 msec per loop
# 211544 function calls in 2.901 seconds
# 1    0.000    0.000    2.901    2.901 les_4_task_1.py:128(find_maximin_3)
# 1    0.133    0.133    2.899    2.899 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_3(300)"
# 100 loops, best of 5: 68 msec per loop
# 475267 function calls in 6.605 seconds
# 1    0.000    0.000    6.605    6.605 les_4_task_1.py:128(find_maximin_3)
# 1    1.411    1.411    6.600    6.600 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_3(400)"
# 100 loops, best of 5: 114 msec per loop
# 845156 function calls in 11.490 seconds
# 1    0.077    0.077   11.489   11.489 les_4_task_1.py:128(find_maximin_3)
# 1    2.358    2.358   11.303   11.303 les_4_task_1.py:4(generate_matrix)

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.find_maximin_3(500)"
# 100 loops, best of 5: 180 msec per loop
# 1320608 function calls in 17.297 seconds
# 1    0.000    0.000   17.296   17.296 les_4_task_1.py:128(find_maximin_3)
# 1    2.972    2.972   16.998   16.998 les_4_task_1.py:4(generate_matrix)


# Вывод:
# 1-й метод имеет эмпирическую оценку O(n**2)
# 2-й и 3-й методы скорее O(n)
# Причем, 3-й метод максимально использует встроенные функции min, ma, map и показывает лучший результат.

# Для учета чистого времени прцедры поиска из основного времени было вычтено время генерации матрицы случайных чисел. Отраженное в 1-й секции.
