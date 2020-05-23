# https://www.hackerrank.com/challenges/any-or-all/problem


def is_palindrome(number):
    return number == number[::-1]


N = int(input())
array = list(input().split())

print(
    all(int(element) >= 0 for element in array)
    and any(is_palindrome(element) for element in array)
)
