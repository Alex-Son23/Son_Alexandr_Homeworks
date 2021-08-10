procent_name = ['процент', 'процента', 'процентов']

for i in range(1, 101):
    if i == 1 or (i > 20 and i % 10 == 1):
        print(f'{i} {procent_name[0]}')
    elif (1 < i < 5) or (1 < i % 10 < 5 and i > 20) :
        print(f'{i} {procent_name[1]}')
    else:
        print(f'{i} {procent_name[2]}')
