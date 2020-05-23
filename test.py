# array = list(map(int, input().split()))
def is_stackable():
    # array = [4, 3, 2, 1, 3, 4]
    array = [1, 3, 2]
    min_index = array.index(min(array))
    print(min_index)


    left_stack = array[0: min_index]
    middle_stack = [array[min_index]]
    right_stack = array[min_index + 1:][::-1]

    print(left_stack, middle_stack, right_stack)

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

    if len(left_stack) > 0:
        for index in range(0, len(left_stack)):
            reverse_index = len(left_stack) - 1 - index
            if left_stack[reverse_index] < middle_stack[len(middle_stack) - 1]:
                return False
            middle_stack.append(left_stack[reverse_index])

    if len(right_stack) > 0:
        for index in range(0, len(right_stack)):
            reverse_index = len(right_stack) - 1 - index
            if right_stack[reverse_index] < middle_stack[len(middle_stack) - 1]:
                return False
            middle_stack.append(right_stack[reverse_index])

    return True


print(is_stackable())
