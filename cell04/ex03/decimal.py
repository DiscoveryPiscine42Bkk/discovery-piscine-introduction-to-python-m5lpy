#!/usr/bin/python3
number = input("Give me a number: ")
if float(number) % 1 == 0:          # float() converts a value into a a decimal number, % 
    print("This number is an integer.")
else:
    print("This number is a decimal.")