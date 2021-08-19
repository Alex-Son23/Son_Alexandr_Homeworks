translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
             'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять',
             'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
             'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'
             }


def num_translate(number):
    word = translate.get(number)
    print(word)

#Я сделал так, т.к. в условии заданчи было показан пример работы программы и там при использовании функции в консоль сразу выводит перевод

def num_translate_adv(number):
    word = translate.get(number)
    print(word)


num_translate('One')
