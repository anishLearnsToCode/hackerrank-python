# https://www.hackerrank.com/challenges/py-set-mutations/problem

_ = input()
A = set(map(int, input().split()))

queries = int(input())

for i in range(queries):
    command = input().split()[0]
    temp = set(map(int, input().split()))

    if command == 'update':
        A.update(temp)
    elif command == 'intersection_update':
        A.intersection_update(temp)
    elif command == 'difference_update':
        A.difference_update(temp)
    else:
        A.symmetric_difference_update(temp)

print(sum(A))
