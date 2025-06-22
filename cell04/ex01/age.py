#!/usr/bin/python3
age = int(input("Please tell me your age:"))
years = [10,20,30]
print("You are currently",age,"years old.")
for year in years:
    print("In", year,"years. you'll be", age + year, "old.")



# ทวน

# for...in reads each value in the array 
# (for example hm = [6,9,10]
#              for i in hm:
#              print(i)
# the output จะประมาณว่า 
# 6
# 9
# 10
# in conclusion "i" is the value that is read, for i in hm: is the hm being reread out

# int means convert something into number if possible