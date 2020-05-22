def get_set():
    return set(map(int, input().split()))


def is_super_set(main, sets):
    for set in sets:
        if not main.issuperset(set):
            return False

    return True


A = get_set()
queries = int(input())
sets = []

for _ in range(queries):
    sets.append(get_set())

print(is_super_set(A, sets))
