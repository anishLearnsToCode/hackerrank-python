def printPattern(pattern, count):
    for j in range(count):
        print(pattern, end='')


n, m = map(int, input().split())

# Upper part
for i in range(n//2):
    printPattern('-', (m-3) // 2 - (3 * i))
    printPattern('.|.', 2 * i + 1)
    printPattern('-', (m - 3) // 2 - (3 * i))
    print()

# Middle part
printPattern('-', (m - 7) // 2)
print('WELCOME', end='')
printPattern('-', (m - 7) // 2)
print()

# Lower Part
for i in range(n // 2):
    printPattern('-', 3 * (i + 1))
    printPattern('.|.', n - 2 * (i + 1))
    printPattern('-', 3 * (i + 1))
    print()
