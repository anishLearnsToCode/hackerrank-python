# https://www.hackerrank.com/challenges/python-lists/problem


queries = int(input())
data = []
for _ in range(queries):
    command, *parameter = input().split()
    parameters = list(map(int, parameter))

    if command == 'insert':
        data.insert(parameters[0], parameters[1])
    elif command == 'print':
        print(data)
    elif command == 'remove':
        data.remove(parameters[0])
    elif command == 'append':
        data.append(parameters[0])
    elif command == 'sort':
        data.sort()
    elif command == 'pop':
        data.pop()
    elif command == 'reverse':
        data.reverse()