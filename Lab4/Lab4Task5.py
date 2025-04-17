letter = input("Enter a letter: ")
if letter in 'aeiou':
    print(f'{letter} is a vowel.')
elif letter.isalpha():
    print(f'{letter} is a consonant.')
else:
    print('Invalid input, please enter a letter')

