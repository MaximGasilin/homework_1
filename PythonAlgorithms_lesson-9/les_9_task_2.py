'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 9.
Задание # 2.

Закодируйте любую строку по алгоритму Хаффмана.
'''

from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def create_Hofman_tree(string):
    symbols = Counter(string)

    if len(symbols) <= 1:
        node = Node(None)

        if len(symbols) == 1:
            node.left = Node(string[0])
            node.right = Node(None)

    while len(symbols) > 1:
        node = Node(None)
        tmp = symbols.most_common()[:-3:-1]

        if isinstance(tmp[0][0], str):
            node.left = Node(tmp[0][0])
        else:
            node.left = tmp[0][0]

        if isinstance(tmp[1][0], str):
            node.right = Node(tmp[1][0])
        else:
            node.right = tmp[1][0]

        symbols[node] = tmp[0][1] + tmp[1][1]

        del symbols[tmp[0][0]]
        del symbols[tmp[1][0]]

    return node


def make_code_table(root, table_of_codes=dict(), code=''):
    if root is None:
        return

    if isinstance(root.value, str):
        table_of_codes[root.value] = code
        return table_of_codes

    make_code_table(root.left, table_of_codes, code + '0')
    make_code_table(root.right, table_of_codes, code + '1')

    return table_of_codes


def str_encode(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


def str_decode(string, codes):
    res = []
    enc_smbl = ''
    for symbol in string:
        enc_smbl += symbol
        for code in codes:
            if codes.get(code) == enc_smbl:
                res.append(code)
                enc_smbl = ''
                break

    return ''.join(res)


var_str = input('Введите пожалуйста строку: ')
# var_str = 'beep boop beer!'
# var_str = ''

h_tree = create_Hofman_tree(var_str)

table_of_codes = make_code_table(h_tree)
print('Таблица кодирования:')
print(f'{table_of_codes}')

enc_string = str_encode(var_str, table_of_codes)
dec_string = str_decode(enc_string, table_of_codes)

print(f'Закодированная по алгоритму Хоффмана строка: {enc_string}')
print(f'Раскодированная строка: {dec_string}')
print(f'Раскодированная строка {"совпадает" if var_str == dec_string else "НЕ совпадает"} с исходной.')