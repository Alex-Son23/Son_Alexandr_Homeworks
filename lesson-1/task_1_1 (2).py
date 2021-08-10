time_factors = [24*60*60, 60*60, 60, 1]
time_types = ['дн', 'час', 'мин', 'сек']
time_types_count = []
seconds = int(input('Введите значение в секундах '))

for i in time_factors:
    time_type_count = seconds // i
    seconds = seconds - time_type_count * i
    time_types_count.append(time_type_count)

final_string = ''

for i, t in time_types_count, time_types:
    count = i
    if count != 0:
        final_string = final_string + count + ' ' + t + ' '

print(final_string)