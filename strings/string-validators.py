def hasalpha(string):
    for character in string:
        if character.isalpha():
            return True

    return False


def hasalnum(string):
    for character in string:
        if character.isalnum():
            return True

    return False


def hasdigit(string):
    for character in string:
        if character.isdigit():
            return True

    return False


def haslower(string):
    for character in string:
        if character.islower():
            return True

    return False


def hasupper(string):
    for character in string:
        if character.isupper():
            return True

    return False


string = input()

print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))
