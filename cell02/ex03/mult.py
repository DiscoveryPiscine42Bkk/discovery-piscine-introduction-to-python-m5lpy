#!/usr/bin/python3

number1 = int(input("Enter the first number :"))           # int means convert something into number if possible

number2 = int(input("Enter the second number :"))
result = number1 * number2
print(str(number1) + "x"+ str(number2) +  "=", result)        # str() changes the numbers into words or strings
if result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is negative.")

# Unnecessary Version
# print("Enter the first number:")
# num1 = int(input())
# print("Enter the second number:")
# num2 = int(input())
# result = int(num1) * int(num2)
# print(int(num1), "x", int(num2), "=", result)

# if result == 0:
#     print("The result is positive and negative.")
# elif result > 0:
#     print("The result is positive.")
# else:
#     print("The result is negative.")