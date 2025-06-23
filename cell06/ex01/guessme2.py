#!/usr/bin/python3
import random
print('''Welcome to the Guess the Number game!\n\nI've generated a secret number between 1 and 100. You have 5 guessed.''')

guessedTimes = 0
generatedNumber = random.randint(1, 100)
win = False
hintMin = 1
hintMax = 100

while guessedTimes < 5:
    print("Attempts left:", 5 - guessedTimes)
    guessedNumber = int(input('Enter your guess: '))
    guessedTimes += 1

    if guessedNumber == generatedNumber:
        win = True
        break
    else:
        if guessedNumber < generatedNumber:
            hintMin = max(hintMin, guessedNumber + 1)         # max() pulls the biggest number out of the array
        else:
            hintMax = min(hintMax, guessedNumber - 1)         # min() pulls the smallest number out of the array

        if guessedTimes < 5:
            print(f'Your guess is not correct. The secret number is between {hintMin} and {hintMax}.')

if win:
    print('Congratulations! You guessed the correct number! 🎉🥳🎊')
else:
    print('''Game Over! You've run out of guesses. The secret number was''', generatedNumber)