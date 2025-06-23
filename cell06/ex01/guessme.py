#!/usr/bin/python3
import random # เอา module random มา
print('''Welcome to the Guess the Number game!\n\nI've generated a secret number between 1 and 100. You have 5 guesses.''')  # \n =  ขึ้นบรรทัดใหม่, ''' just makes it look cleaner in this part
guessedTimes = 0        # This counts how many times the user has guessed, starts at 0, increases with each guess
generatedNumber = random.randint(1,100)         # generates random number between 1-100 (stands for random integer)
win = False         # Starts as False, becomes True if they guess the number right
while guessedTimes < 5:         # ถ้า guessedTimes ไม่เกิน 5 ให้รัน / The loop runs as long as they've guessed less than 5 times
    print("Attempts left:", 5 - guessedTimes)
    guessedNumber = int(input('Enter your guess: '))
    guessedTimes += 1
    if guessedNumber == generatedNumber: # ถ้าถูกให้ปรับ win เป็น True
        win = True
        break # ละจบ script
    else: # ถ้าไม่ถูก
        if not generatedNumber == 100: # ถ้าเลขที่เจนมาไม่ใช่ 100 ให้รันโค้ดนี้
            randomNumber = generatedNumber + random.randint(1, 100 - generatedNumber)
        else: # ถ้าเลขที่เจนมาคือ 100 ให้รันโค้ดนี้
            randomNumber = generatedNumber
        if guessedTimes < 5: # ถ้า guessedTime ยังไม่เกิน 5 ให้รันโค้ดนี้
            print('Your guess is not correct. The secret number is between 1 and', randomNumber)
if win: # print ชนะหรือไม่ชนะ
    print('Congratulations! You guessed the correct number! 🎉🥳🎊')
else:
    print('''Game Over! You've run out of guesses. The secret number was''', generatedNumber)