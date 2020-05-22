import string

rangoli = []
size = int(input())
for i in range(size):
    line = '-'.join(string.ascii_lowercase[size - i - 1:size])
    decreasing = line[::-1]
    increasing = line[1:]
    pattern = (decreasing + increasing).center(4 * size - 3, '-')
    rangoli.append(pattern)

inverted = rangoli[0:size - 1][::-1]
# print(inverted)

for i in range(len(rangoli)):
    print(rangoli[i])

for i in range(len(inverted)):
    print(inverted[i])
    