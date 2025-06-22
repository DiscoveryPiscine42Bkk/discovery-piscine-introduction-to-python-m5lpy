#!/usr/bin/python3

print("Enter a number")
number = int(input())       # int means convert something into number if possible
multiplier = 0

while multiplier < 9:
  result = number * multiplier
  print(number, "x", multiplier, "=", result)
  multiplier += 1
  if multiplier == 9:
    break         # used to exit a loop early
