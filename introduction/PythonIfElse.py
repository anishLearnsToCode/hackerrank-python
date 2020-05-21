number = int(input())

if number % 2 == 1:
    print('Weird')
elif 2 <= number <= 5:
    print('Not Weird')
elif 6 <= number <= 20:
    print('Weird')
elif number > 20:
    print('Not Weird')
