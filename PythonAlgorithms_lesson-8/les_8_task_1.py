'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 8.
Задание # 1.

На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''


def counting_handshakes_graph(count):
    result = []
    i = 0
    while i < count:
        j = 0
        while j < count:
            if i != j:
                result.append((i, j))
            j += 1
        i += 1
    return result


if __name__ == '__main__':
    n = int(input('Укажите пожалуйста количество друзей: '))
    graph = counting_handshakes_graph(n)
    print(*graph)
    print(f'При встрече было {len(graph)} рукопожатий.')
