# Declare two variables and print which variable is largest using ternary operators
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(a if a > b else b)
except ValueError:
    print("Invalid input! Please enter numeric values.")
2
