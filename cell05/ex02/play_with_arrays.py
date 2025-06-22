#!/usr/bin/python3
array =  [2,8,9,48,8,22,-12,2]
newArray = []           # Creates an empty list called newArray
for number in array:
    if number + 2 > 5:        # line 4 and 5 makes it so that if number is more than 5 after +2 it is processed
        newArray.append(number + 2)
print("Original Array:", array)
print("New array:", newArray)