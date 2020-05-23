# https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, input().split())
data = []
for _ in range(X):
    subject_marks = list(map(float, input().split()))
    data.append(subject_marks)

tuples = zip(*data)
for element in tuples:
    print(sum(element) / X)
