import datetime

date_format = '%a %d %b %Y %X %z'
queries = int(input())

for _ in range(queries):
    date1 = datetime.datetime.strptime(input(), date_format)
    date2 = datetime.datetime.strptime(input(), date_format)
    diff = int(abs((date2 - date1).total_seconds()))
    print(diff)
