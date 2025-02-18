# 1. Calculate the multiplication and sum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2
sum_of_numbers = num1 + num2

print(f"Multiplication: {multiplication}")
print(f"Sum: {sum_of_numbers}")


# 2. Declare two variables and print that which variable is largest using ternary operators
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

largest = a if a > b else b
print(f"The largest number is: {largest}")


# 3. Python program to convert the temperature in degree centigrade to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")



# 4. Python program to find the area of a triangle whose sides are given
a = float(input("Enter side a of the triangle: "))
b = float(input("Enter side b of the triangle: "))
c = float(input("Enter side c of the triangle: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle is: {area}")
