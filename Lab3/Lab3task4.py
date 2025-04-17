salary = int(input('Enter your salary: '))
years = int(input('Enter service years: '))

if years > 5:
    bonus = salary * 0.05
    print(f'your net bonus amount is {bonus}')
else:
    print('As your service years are not more than 5. So, you dont get any bonus')