import re

pattern = '([a-z]|[A-Z]|\d|_|-)+@([a-z]|[A-Z]|\d)*[.].{1,3}'


def fun(email):
    match = re.fullmatch(pattern, email)
    if match is not None:
        return match.span() == (0, len(email))


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
