# https://www.hackerrank.com/challenges/finding-the-percentage/problem


def average(marks):
    return "{0:.2f}".format(sum(marks) / 3)


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores


query_name = input()
print(average(student_marks[query_name]))
