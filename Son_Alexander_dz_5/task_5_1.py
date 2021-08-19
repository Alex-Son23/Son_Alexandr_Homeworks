def odd_nums(num):
    for i in range(1, num + 1, 2):\
        yield i

odd_to_15 = odd_nums(15)

for i in odd_to_15:
    print(i)