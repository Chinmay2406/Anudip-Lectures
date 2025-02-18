#Python program that prompts the user to input two numbers and raises a 
# TypeError exception if the inputs are not numerical:

try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if not num1.isdigit() or not num2.isdigit():
        raise TypeError("Both inputs must be numerical.")
    
    num1 = int(num1)
    num2 = int(num2)
    
    print(f"Sum: {num1 + num2}")
    
except TypeError as e:
    print(e)

if num1.isdigit() and num2.isdigit():
    print(f"Both inputs '{num1}' and '{num2}' are valid integers.")
else:
    print("One or both inputs are not valid integers.")
