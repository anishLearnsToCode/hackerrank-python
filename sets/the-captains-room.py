# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
array = list(map(int, input().split()))

frequencies = dict()

for element in array:
    frequencies[element] = (frequencies[element] if element in frequencies else 0) + 1

for key in frequencies:
    if frequencies[key] == 1:
        print(key)
        break
