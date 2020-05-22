def remove_duplicates(word):
    letters = {}
    result = ''
    for letter in word:
        if letter not in letters:
            result += letter
            letters[letter] = True

    return result


def print_segments(line, k):
    chunk = len(line) // k
    words = [line[i: i + chunk] for i in range(0, len(line), chunk)]

    for i in range(len(words)):
        words[i] = remove_duplicates(words[i])

    for word in words:
        print(word)


line = input()
k = int(input())

print_segments(line, k)
