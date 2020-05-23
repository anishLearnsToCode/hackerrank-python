import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


queries = int(input())
for _ in range(queries):
    regex = input()
    print(is_valid_regex(regex))
