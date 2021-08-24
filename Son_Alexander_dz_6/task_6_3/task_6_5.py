import itertools
import sys

names = sys.argv

# print(sys.argv)

users_hobbies = {}
users = [
    'Сон,Александр,Романович\n',
    'Панфилкин,Михаил,Евгеньевич\n',
    'Маржовский,Иван,Отчествонезнаю\n',
    'Наталья,Морская,Пехота\n',
    'Иванов,Иван,Иванович'
         ]
hobbies = [
    'программирование\n',
    'лень\n',
    'обучение языку программирования Python\n',
    'ZXC'
]

with open(names[1], 'w', encoding='UTF-8') as f:
    f.writelines(users)
    # for user in f:
    #     users.append(user.strip().replace(',', ' '))

with open(names[2], 'w', encoding='UTF-8') as f:
    f.writelines(hobbies)
    # for hobby in f:
    #     hobbies_list.append(hobby.strip().replace(',', ' '))

for i, hobby in enumerate(hobbies):
    hobbies[i] = hobby.strip().replace(',', ' ')
for i, user in enumerate(users):
    users[i] = user.strip().replace(',', ' ')

with open(names[3], 'w', encoding='UTF-8') as f:
    for user, hobby in itertools.zip_longest(users, hobbies):
        if hobby is None:
            f.write(f'{user}: {None} \n')
        elif user is None:
            break
        else:
            f.write(f'{user}: {hobby} \n')
            # users_data[key] = val.replace('\n', '')
#
# print(users_hobbies)
# print(users)
# print(hobbies)
