import itertools
import sys



users_hobbies = {}
users = []
hobbies = []

with open('users.csv', 'r+', encoding='UTF-8') as f:
    for user in f:
        users.append(user.strip().replace(',', ' '))

with open('hobby.csv', 'r', encoding='UTF-8') as f:
    for hobby in f:
        hobbies.append(hobby.strip().replace(',', ' '))

# for key, val in itertools.zip_longest(users, hobbies_list):
#     if val is None:
#         users_data[key] = None
#     elif key is None:
#         break
#     else:
#         users_data[key] = val.replace('\n', '')

with open('users_hobby.txt', 'w', encoding='UTF-8') as f:
    for user, hobby in itertools.zip_longest(users, hobbies):
        if hobby is None:
            f.write(f'{user}: {None} \n')
        elif user is None:
            break
        else:
            f.write(f'{user}: {hobby} \n')
            # users_data[key] = val.replace('\n', '')

print(users_hobbies)
print(users)
print(hobbies)
