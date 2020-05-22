import itertools

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

result = list(itertools.product(array1, array2))

for entry in result:
    print(str(entry) + ' ', end='')
