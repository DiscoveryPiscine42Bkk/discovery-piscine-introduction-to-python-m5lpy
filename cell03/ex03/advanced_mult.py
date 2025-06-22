#!/usr/bin/python3
numberSet = [0,1,2,3,4,5,6,7,8,9,10]
for number in numberSet:
    multiplyTable = [0]             # [] is for creating a list
    for i in range(10):
        plusNumber = multiplyTable[-1] + number             # [-1] means get the last item on the list (So if multiplyTable = [0, 3, 6], then multiplyTable[-1] is 6)
        multiplyTable.append(plusNumber)
    print("Table", number,multiplyTable)

# this inner loop 1. takes the last number from the list: multiplyTable[-1]     2. adds the current number (from numberSet)     3. connects the result to the list


# for...in reads each value in the array 
# (for example hm = [6,9,10]
#              for i in hm:
#              print(i)
# the output จะประมาณว่า 
# 6
# 9
# 10
# in conclusion "i" is the value that is read, for i in hm: is the hm being reread out