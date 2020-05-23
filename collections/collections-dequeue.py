# https://www.hackerrank.com/challenges/py-collections-deque/problem

import collections

queue = collections.deque()

queries = int(input())

for _ in range(queries):
    line = input()
    if line == 'pop':
        queue.pop()
    elif line == 'popleft':
        queue.popleft()
    else:
        line = line.split()
        command = line[0]
        element = int(line[1])
        if command == 'append':
            queue.append(element)
        else:
            queue.appendleft(element)

for element in queue:
    print(element, end=' ')
