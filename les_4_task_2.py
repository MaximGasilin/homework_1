'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 4.
Задание # 2.

Поиск простых чисел среди n натуральных чисел. Методом Решета Эратосфена и классическим перебором.

Вывод
  Проведенный анализ показывает эмпирическую сложность классического алгоритма O(n**2)  О от Эн в квадрате
  Проведенный анализ показывает эмпирическую сложность алгоритма "Решето Эратосфена" O(n)  О от Эн.
  Более подробно можно посмотреть страницу "Решето" в прикрепленном к задаче эксельном файле.
  Файл не содерижт макросов или вирусов.
'''

import cProfile

# def test_prime(func):
#     lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
#     67,	71, 73,	79,	83,	89,	97,	101, 103, 107, 109, 113, 127, 131, 137,	139,
#     149, 151, 157, 163,	167, 173, 179, 181,	191, 193, 197, 199, 211, 223, 227,
#     229, 233, 239, 241, 251, 257, 263, 269,	271, 277, 281, 283,	293, 307, 311,
#     313, 317, 331, 337,	347, 349, 353, 359,	367, 373, 379, 383,	389, 397, 401,
#     409, 419, 421, 431, 433, 439, 443, 449,	457, 461, 463, 467,	479, 487, 491,
#     499, 503, 509, 521, 523, 541, 547, 557,	563, 569, 571, 577, 587, 593, 599,
#     601, 607, 613, 617,	619, 631, 641, 643,	647, 653, 659, 661,	673, 677, 683,
#     691, 701, 709, 719,	727, 733, 739, 743,	751, 757, 761, 769,	773, 787, 797,
#     809, 811, 821, 823,	827, 829, 839, 853,	857, 859, 863, 877,	881, 883, 887,
#     907, 911, 919, 929,	937, 941, 947, 953,	967, 971, 977, 983,	991, 997]

#     for i in range(2, 1001):
#         for j, item in enumerate(func(i)):
#             assert item == lst[j]
#         print(f"Test {i} OK!")


def classic(limit):
    result = []
    for i in range(2, limit + 1):
        for el in result:
            if i % el == 0:
                break
        else:
            result.append(i)

    return result

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.classic(100)"
# 1000 loops, best of 3: 24.7 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.classic(500)"
# 1000 loops, best of 3: 252 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.classic(800)"
# 1000 loops, best of 3: 590 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.classic(1000)"
# 1000 loops, best of 3: 804 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.classic(1500)"
# 1000 loops, best of 3: 1.49 msec per loop

# cProfile.run('classic(100)')
# 29 function calls in 0.000 seconds
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('classic(500)')
# 99 function calls in 0.000 seconds
# 95    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('classic(800)')
# 143 function calls in 0.001 seconds
# 139    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('classic(1000)')
# 172 function calls in 0.001 seconds
# 168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('classic(1500)')
# 243 function calls in 0.003 seconds
# 239    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#  Проведенный анализ показывает эмпирическую сложность алгоритма O(n**2)  О от Эн в квадрате
#  Более подробно можно посмотреть страницу "Решето" в прикрепленном к задаче эксельном файле.
#  Файл не содерижт макросов или вирусов.

def sieve(limit):
    sieve_of_e = [i for i in range(limit)]
    sieve_of_e[1] = 0

    for i in range(2, limit):
        if sieve_of_e[i] != 0:
            j = i * 2
            while j < limit:
                sieve_of_e[j] = 0
                j += i

    result = [i for i in sieve_of_e if i != 0]

    return result

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(100)"
# 100 loops, best of 3: 18.1 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(500)"
# 100 loops, best of 3: 119 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(800)"
# 100 loops, best of 3: 228 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(1000)"
# 100 loops, best of 3: 270 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(1500)"
# 1000 loops, best of 3: 356 usec per loop


# cProfile.run('sieve(100)')
# 6 function calls in 0.000 seconds

# cProfile.run('sieve(500)')
# 6 function calls in 0.000 seconds

# cProfile.run('sieve(800)')
# 6 function calls in 0.001 second

# cProfile.run('sieve(1000)')
# 6 function calls in 0.001 seconds

# cProfile.run('sieve(1500)')
# 6 function calls in 0.001 seconds

#  Проведенный анализ показывает эмпирическую сложность алгоритма O(n)  О от Эн.
#  Более подробно можно посмотреть страницу "Решето" в прикрепленном к задаче эксельном файле.
#  Файл не содерижт макросов или вирусов.


if __name__ == '__main__':
    # test_prime(sieve)
    # test_prime(classic)

    # cProfile.run('sieve(100)')
    # cProfile.run('sieve(500)')
    # cProfile.run('sieve(800)')
    # cProfile.run('sieve(1000)')
    # cProfile.run('sieve(1500)')

    # cProfile.run('classic(100)')
    # cProfile.run('classicclassic(500)')
    # cProfile.run('classic(800)')
    # cProfile.run('classic(1000)')
    # cProfile.run('classic(1500)')
