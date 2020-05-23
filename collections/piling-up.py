# https://www.hackerrank.com/challenges/piling-up/problem

def get_list():
    return list(map(int, input().split()))


def can_clear_stack(stack, array):
    if len(stack) > 0:
        for index in range(0, len(stack)):
            reverse_index = len(stack) - 1 - index
            if stack[reverse_index] < array[len(array) - 1]:
                return False
            array.append(stack[reverse_index])

    return True


def is_stackable(array):
    min_index = array.index(min(array))
    left_stack = array[0: min_index]
    middle_stack = [array[min_index]]
    right_stack = array[min_index + 1:][::-1]

    i = len(left_stack) - 1
    j = len(right_stack) - 1

    while i >= 0 and j >= 0:
        next = min(left_stack[i], right_stack[j])
        if next >= middle_stack[len(middle_stack) - 1]:
            middle_stack.append(next)
            if next == left_stack[i]:
                left_stack.pop()
                i -= 1
            else:
                right_stack.pop()
                j -= 1
        else:
            return False

    return can_clear_stack(left_stack, middle_stack) and can_clear_stack(right_stack, middle_stack)


queries = int(input())

for _ in range(queries):
    input()
    array = get_list()
    if is_stackable(array):
        print("Yes")
    else:
        print("No")
