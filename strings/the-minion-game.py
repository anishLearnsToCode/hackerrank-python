consonants = [
    'b', 'c', 'd', 'f', 'g',
    'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's',
    't', 'v', 'w', 'x', 'y',
    'z'
]

vowels = ['A', 'E', 'I', 'O', 'U']


def get_vowel_score(word):
    score = 0
    for i in range(len(word)):
        if word[i] in vowels:
            score += len(word) - i
    return score


def get_consonant_score(word):
    score = 0
    for i in range(len(word)):
        if word[i] not in vowels:
            score += len(word) - i
    return score


word = input()

score_consonant = get_consonant_score(word)
score_vowel = get_vowel_score(word)

if score_consonant > score_vowel:
    print('Stuart ' + str(score_consonant))
elif score_consonant < score_vowel:
    print('kevin ' + str(score_vowel))
else:
    print('Draw')
