#!/usr/bin/python3
print("Enter a number less than 25")
user_input_num = int(input())
# variable = input("prompt")

if user_input_num < 25 :
    count = user_input_num
    while count <= 25:
        print(f"Inside the loop, my variable is {count}")           # f-string (f...) is for printing variables nicely, whatever inside {} will be repeated until the loop ends
        count += 1
else:
    print("Error")