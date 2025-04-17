num = int(input('Enter any number: '))

if num < 0:
    print(f'{num} is a negative number.')
elif num < 10:
    print(f'{num} is one digit number.')
elif num < 100:
    print(f'{num} is two digit number.')
elif num < 1000:
    print(f'{num} is three digit number.')
else:
    print(f'{num} is more than three digit number.')