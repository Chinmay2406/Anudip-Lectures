# Program to handle ZeroDivisionError and accept other numbers
try:
    num = int(input("Enter a number: "))
    divisor = int(input("Enter the divisor: "))
    result = num / divisor
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result: {result}")


# 2. ValueError Handling -Python program that prompts the user to input an integer and raises a 
#                         ValueError exception if the input is not a valid integer:
user_input = input("Enter an integer: ")

try:
    num = int(user_input)
    print(f"You entered a valid integer: {num}")
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer. Please enter a valid integer.")



#Program to accept choice from user and perform the operation:

# 3. Accept choice from user and perform the operation

print("Choose an operation:")
print("a. Try except")
print("b. Try multiple except")
print("c. Try except else")
print("d. Finally")
print("e. Try single except")
print("f. Raising exception")

choice = input("Enter a choice (a-f): ")

# a. Try except
if choice == 'a':
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# b. Try multiple except
elif choice == 'b':
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# c. Try except else
elif choice == 'c':
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {result}")

# d. Finally
elif choice == 'd':
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("This block will always execute.")

# e. Try single except
elif choice == 'e':
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except Exception as e:
        print(f"An error occurred: {e}")

# f. Raising exception
elif choice == 'f':
    try:
        num = int(input("Enter a number: "))
        if num == 0:
            raise ValueError("You cannot enter zero.")
        result = 10 / num
    except ValueError as e:
        print(e)



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
