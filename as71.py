# 1. WAP to find greatest among two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

greatest = num1 if num1 > num2 else num2
print(f"The greatest number is: {greatest}")
