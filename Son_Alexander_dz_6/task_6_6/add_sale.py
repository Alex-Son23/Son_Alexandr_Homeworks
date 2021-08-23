import sys


def add_purchase(purchase):
    with open('income.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{purchase[1]}\n')

add_purchase(sys.argv)
