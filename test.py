import itertools

word = 'aaaabbcaaabddeffg'

for entry in itertools.groupby(word):
    for element in entry[1]:
        print(element, end='')
    print()
