line = input()
words = line.split()
for word in words:
    line = line.replace(word, word.capitalize())

print(line)
