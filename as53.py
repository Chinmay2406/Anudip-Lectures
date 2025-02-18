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
