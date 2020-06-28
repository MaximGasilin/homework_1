'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 8.
Задание # 3.

Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

import random


def generate_graph(count):
    graph = []

    for i in range(count):
        edges = random.sample(range(0, count), random.randint(1, count - 1))
        for el in edges:
            if i == el:
                edges.remove(el)  # удаление циклов при генерации графа
        graph.append(edges)

    return graph


def dfs(graph, start, target, visited=[]):

    result = False

    if len(visited) == 0:
        cnt = 0
        while cnt < len(graph):
            visited.append(False)
            cnt += 1
    visited[start] = True

    for el in graph[start]:
        if el == target:
            return True
        if not visited[el]:
            result = dfs(graph, el, target, visited)
            if result:
                return True

    return result


if __name__ == '__main__':
    count = 7 # int(input('Укажите пожалуйста количество вершин графа: '))
    graph = generate_graph(count)
    print(*graph)

    visited = [] #Если не указать этот список до запуска, то не будет возможности отследить, по каким вершинам прошлись.
    start = 0
    target = 3

    result = dfs(graph, start, target, visited)
    print(visited)
    if result:
        print(f'Из вершины {start} ДОБРАЛСЯ до вершины {target} посетив {[el for el in range(0, count) if visited[el]]}.')
    else:
        print(f'Из вершины {start} НЕЛЬЗЯ добраться до вершины {target}.')
