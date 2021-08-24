import sys


def show_purchases(start_stop):
    if len(start_stop) == 2:
        start = 0
        start_line = int(start_stop[1]) - 1
        with open('income.txt', 'r') as f:
            for i in range(start_line):
                start += len(f.readline())
            f.seek(start)
            print(f.read())
    elif len(start_stop) == 1:
        with open('income.txt', 'r') as f:
            print(f.read())
    else:
        start = 0
        end_line = int(start_stop[2])
        start_line = int(start_stop[1]) - 1
        with open('income.txt', 'r') as f:
            for i in range(start_line):
                start += len(f.readline())
            f.seek(start)
            for i in range(end_line):
                print(f.readline().strip())


show_purchases(sys.argv)
