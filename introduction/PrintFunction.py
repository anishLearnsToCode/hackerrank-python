# https://www.hackerrank.com/challenges/python-print/problem


def print_numbers(number):
    string = ''
    for i in range(number):
        string += str(i + 1)
    print(string)


number = int(input())
print_numbers(number)
