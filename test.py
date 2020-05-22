line, k = input(), int(input())

iterator = line.__iter__()
iterators = zip(*([iterator] * k))

for word in iterators:
    d = dict()
    result = ''.join([d.setdefault(letter, letter) for letter in word if letter not in d])
    print(result)
