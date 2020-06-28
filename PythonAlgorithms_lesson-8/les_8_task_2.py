'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 8.
Задание # 2.

Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.

Немного странная задача. Т.к. по своей сути массив parent уже содержит всю необходимую информацию, но в сжатом виде.
Необходимо его "распарсить" (расшифровать).

Поэтому решил задачу 2-мя методами:
1-й: Распарсил массив parent. Т.е. пробежался по нему и углубился для каждой вершины настолько, насколько было нужно.
2-й: Встроился в текущий алгоритм. И если вдруг мы находим более короткий путь до вершины, то копируем этот короткий
маршрут, вместо старого.

В конце возвращаем полученный путь.
'''

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start_vertex):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    topology = [] # кратчайшие пути

    start = start_vertex
    cost[start] = 0
    min_cost = 0
    cnt = 0
    while cnt < length:
        topology.append([])
        cnt += 1
    topology[start].append(start)

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    # Второй вариант. Каждый раз находя более короткий путь - заменяем набор старых вершин - на новый.
                    topology[i] = topology[start].copy()
                    topology[i].append(i)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    # Первый вариант. Основанный на том, что в массиве parent находится вершина, путь от которой до нашей стоил
    # дешевле всего. Поэтому нужно вытащить данные из этого массива. И все.
    # cnt = 0
    # while cnt < length:
    #     idx = cnt
    #     while parent[idx] != -1:
    #         topology[cnt].insert(0, parent[idx])
    #         idx = parent[idx]
    #     if len(topology[cnt]) == 0 and cnt != start_vertex:
    #         topology[cnt].append(float('inf'))
    #     else:
    #         topology[cnt].append(cnt)
    #     cnt += 1

    return (cost, topology)


start = int(input('От какой вершины идти:'))
res = dijkstra(graph, start)
cost, topology = res[0], res[1]
print(cost, '\n', topology)
