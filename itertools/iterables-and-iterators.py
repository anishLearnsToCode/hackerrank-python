# https://www.hackerrank.com/challenges/iterables-and-iterators/problem


def compute(value, count):
    result = 1
    for i in range(count):
        result *= value - i
    return result


def number_of_a(array):
    count = 0
    for element in array:
        if element == 'a':
            count += 1
    return count


N = int(input())
array = input().split()
k = int(input())
n = number_of_a(array)

numerator = compute(N - n, k)
denominator = compute(N, k)
probability = 1 - numerator / denominator
print(probability)
