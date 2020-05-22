def wrap(string, max_width):
    paragraph = ''
    count = 0
    for i in range(len(string)):
        if i % max_width == 0 and i != 0:
            paragraph += '\n'
        paragraph += string[i]
    return paragraph


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
