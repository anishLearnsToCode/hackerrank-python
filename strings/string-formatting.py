n: int = int(input())
width = len('{0:b}'.format(n))

for i in range(1, n + 1):
    print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))
