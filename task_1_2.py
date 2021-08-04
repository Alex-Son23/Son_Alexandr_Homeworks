cube_x = []
sum_numbers = 0

for cube in range(1, 1001, 2):
    cube = cube ** 3
    cube_x.append(cube)
    sum_number = 0
    while cube != 0:
        digit = cube % 10
        sum_number += digit
        cube = cube // 10
    if sum_number % 7 == 0:
        sum_numbers += sum_number

# print(cube_x)
print(sum_numbers)

sum_numbers = 0
n = 0

while n != len(cube_x):
    cube_x[n] += 17
    new_cube = cube_x[n]
    while new_cube > 0:
        digit = new_cube % 10
        sum_number += digit
        new_cube = new_cube // 10
    if sum_number % 7 == 0:
        sum_numbers += sum_number
    n += 1

# ВАЖНО
# Хотел бы спросить как можно было выполнить задание 2.b используя цикл for?
# ВАЖНО

# print(cube_x)
print(sum_numbers)
