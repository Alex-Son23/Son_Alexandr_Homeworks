time_values = [24* 60 ** 2, 60 ** 2, 60, 1]
time_names = ['дн', 'час', 'мин', 'сек']
time_comfort = []
seconds = int(input('Введите количестов секунд '))

for time_value in time_values:
    time_index = seconds // time_value
    seconds = seconds - time_index * time_value
    time_comfort.append(time_index)

# print(time_comfort)

final_string = ''
n = 0

while n != len(time_names):
    if time_comfort[n] != 0:
        final_string = f'{final_string} {time_comfort[n]} {time_names[n]}'
    n += 1

#ВАЖНО
#Можео было бы сделать второй цикл не while, а for?
#ВАЖНО

# for time, name in time_comfort, time_names:
#     count = time
#     if time != 0:
#         final_string = f'{final_string} {count} {name}'

print(final_string)
