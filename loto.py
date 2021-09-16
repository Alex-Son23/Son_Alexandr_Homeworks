from random import randint, choice, shuffle
from abc import ABC, abstractmethod
from time import sleep

def get_keg_numbers_list():
    kegs = [i for i in range(1, 91)]
    kegs_list = []
    for _ in range(0, 15):
        count = 1
        while count != 0:
            keg_number = choice(kegs)
            count = kegs_list.count(keg_number)
            if count == 0:
                kegs_list.append(keg_number)
    kegs_list[:5] = sorted(kegs_list[:5])
    kegs_list[5:10] = sorted(kegs_list[5:10])
    kegs_list[10:15] = sorted(kegs_list[10:15])
    return kegs_list


class Card(ABC):

    def __init__(self, name):
        self.name = name
        self.kegs_list = get_keg_numbers_list()
        self._gaps = [randint(1, 3) for _ in range(1, 15)]

    def __str__(self):
        str_card = ''

        for space, keg_number in zip(self._gaps[:5], self.kegs_list[:5]):
            str_card += space * ' ' + str(keg_number)
        str_card += '\n'

        for space, keg_number in zip(self._gaps[5:10], self.kegs_list[5:10]):
            str_card += space * ' ' + str(keg_number)
        str_card += '\n'

        for space, keg_number in zip(self._gaps[10:], self.kegs_list[10:]):
            str_card += space * ' ' + str(keg_number)
        str_card += ' ' * self._gaps[-1] + str(self.kegs_list[14]) + '\n'

        dashes = 26 - len(self.name) - 2
        first_string = '-' * (dashes // 2) + ' ' + self.name + ' ' + '-' * (dashes // 2) + '\n'
        return first_string + str_card + '-' * 26

    def __sub__(self, other):
        keg_index = self.kegs_list.index(keg_val)
        self.kegs_list.remove(keg_val)
        self.kegs_list.insert(keg_index, '-')


computer_card = Card('Computer Card')
player_card = Card('Player Card')

kegs = [i for i in range(1, 91)]
shuffle(kegs)

for i, keg_val in enumerate(kegs):

    number = 99 - (i + 1)

    print(f'Новый бочонок: {keg_val} (осталось {number})\n{player_card}\n{computer_card}')
    answer = input('Зачеркнуть цифру? (y/n)\n')

    # For player
    if answer.lower() == 'y':
        if player_card.kegs_list.count(keg_val) == 1:
            player_card - keg_val
        else:
            print('Вы проиграли')
            sleep(5)
            break
    elif answer.lower() == 'n':
        if player_card.kegs_list.count(keg_val) == 1:
            print('Вы проиграли')
            sleep(5)
            break
    else:
        if player_card.kegs_list.count(keg_val) == 1:
            print('Вы проиграли')
            sleep(5)
            break

    if player_card.kegs_list.count('-') == 15:
        print('Победа!!!')
        sleep(5)
        break

    # For computer

    if computer_card.kegs_list.count(keg_val) == 1:
        computer_card - keg_val

    if computer_card.kegs_list.count('-') == 15:
        print('Победа комрьютера!!!')
        sleep(5)
        break
