# https://www.hackerrank.com/challenges/python-tuples/problem


length = int(input())
tokens = input().split()
data = list(map(int, tokens))
t = tuple(data)
print(hash(t))
