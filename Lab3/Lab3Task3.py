length = int(input('Enter length: '))
width = int(input('Enter width: '))

if length == width:
    print(f'{length} and {width} are sides of a square.')
else:
    print(f'{length} and {width} are sides of a rectangle.')