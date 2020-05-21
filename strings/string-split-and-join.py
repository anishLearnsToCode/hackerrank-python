def split_and_join(string):
    tokens = string.split()
    return '-'.join(tokens)


string = input()
print(split_and_join(string))