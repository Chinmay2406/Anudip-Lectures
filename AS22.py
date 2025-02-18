a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a  # Swapping using tuple unpacking
print(f"After swapping: a = {a}, b = {b}")
3