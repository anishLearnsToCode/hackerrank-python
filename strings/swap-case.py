# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    result = ""
    for let in s:
        if let.isupper():
            result += let.lower()
        else:
            result += let.upper()
    return result


string = input()
print(swap_case(string))
