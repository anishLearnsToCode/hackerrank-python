# https://www.hackerrank.com/challenges/nested-list/problem

def get_grade(element):
    return element[1]


def get_second_min_grade(array, min_grade):
    for i in range(len(array)):
        if array[i][1] != min_grade:
            return array[i][1]


def get_names_with_second_min_grade(array, second_min_grade):
    names = []
    for i in range(len(array)):
        if array[i][1] == second_min_grade:
            names.append(array[i][0])

    return names


students = int(input())
data = []

for i in range(students):
    name = input()
    grade = float(input())
    data.append([name, grade])

data.sort(key=get_grade)
min_grade = data[0][1]
print('min grade:', min_grade)

second_min_grade = get_second_min_grade(data, min_grade)
print('second min:', second_min_grade)

names_with_second_min_grade =  sorted(get_names_with_second_min_grade(data, second_min_grade))

for name in names_with_second_min_grade:
    print(name)
