#!/usr/bin/python3
array =  [2,8,9,48,8,22,-12,2]
newArray = []           # Creates an empty list called newArray
for number in array:
    newArray.append(number + 2)         # Takes the current number, adds 2 to it
print("Original Array:", array)
print("New array:", newArray)