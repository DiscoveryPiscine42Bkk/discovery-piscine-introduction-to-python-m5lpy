#!/usr/bin/python3
numberOne = int(input("Give me the first number:"))
numberTwo = int(input("Give me the second number:"))
mathArray = {"+","-","/","*"}           # despite putting the +,-,/,* into "", it could still be calculated because there's eval(), which converts stuff into actual math
for math in mathArray:                  # an array is a collection of items
    mathString = str(numberOne) + math + str(numberTwo)            # str() is convert a text into number
    print(numberOne, math, numberTwo, eval(mathString))         # eval() for example if I put 69/9 it will convert into math calculation