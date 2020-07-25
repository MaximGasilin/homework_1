'''
Курс "Алгоритмы и структуры данных на Python."
Урок # 5.
Задание # 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.

P.S.: Эту задачу можно легко решить и при помщи обычных методов, но я решил использовать мксимально возможное количество
новых сущьностией и модуля collections. Удалось использовать namedtuple, Counter, ChainMap
'''

from collections import namedtuple, Counter, ChainMap
from functools import reduce
from random import randint


def generate_company_profit(quantity):
    '''
    Генерирует тестовый пример для отладки алгоритма, который решает поставленную задачу

    :param quantity: количество компаний, которые потом будем сравнивать
    :return: сгенерированный Counter который хранит название компаний и их прибыль
    '''
    Firm = namedtuple('Firm', 'name, profit')
    result = Counter(dict([Firm(f'Firm_{counter}', randint(50000, 100000)) for counter in range(quantity)]))
    return result


def input_company_profit():
    '''
    Считывет данный, которые вводит пользователь и преобразует их в Counter

    :return: ввести пользовательские данные и сформировать Counter который хранит название компаний и их прибыль
    '''
    Firm = namedtuple('Firm', 'name, profit')
    firm_count = int(input('Введите пожалуйста количество предприятий: '))
    entered_data = []
    for i in range(1, firm_count + 1):
        firm_name = input(f'Введите название {i} компании: ')
        firm_profit = list(map(float, input(f'Введите прибыль {i} компании за 4 квартала через пробел: ').split()))
        entered_data.append(Firm(f'{firm_name}', sum(firm_profit)))
        result = Counter(dict(entered_data))
    return result


def output_result_information(chain_map):
    print('-' * 50)
    print(f'Средняя годовая прибыль компании из списка равна: {chain_map.maps[2]["Average profit"]}')
    print('Прибыль ВЫШЕ среднего у компаний:')
    winners_str = reduce(lambda res_str, el: f'{res_str}, {el[0]} ({el[1]})', chain_map.maps[0].items(), ',')
    winners_str = winners_str.replace(',, ', '')
    print(winners_str)
    print('Прибыль НИЖЕ среднего у компаний:')
    losers_str = reduce(lambda res_str, el: f'{res_str}, {el[0]} ({el[1]})', chain_map.maps[1].items(), ',')
    losers_str = losers_str.replace(',, ', '')
    print(losers_str)

# profit_dict = generate_company_profit(5)
profit_dict = input_company_profit()

# Сортировка, на всякий случай.
sorted(profit_dict, key=profit_dict.get)

# Расчет среднего значения прибыли
average_value = sum(profit_dict.values()) / len(profit_dict)
# Количество компаний, с прибылью больше средней
average_limit = reduce(lambda x, el: x + (1 if el >= average_value else 0), profit_dict.values(), 0)

# В первый список перенесем информацию о тех, кто получил результаы выше среднего
winners = Counter(dict(profit_dict.most_common(average_limit)))
losers = profit_dict - winners
firms_list = ChainMap(winners, losers, Counter({'Average profit': average_value}))

print(firms_list)
output_result_information(firms_list)
