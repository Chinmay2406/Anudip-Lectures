# 4. Python program to find the area of a triangle whose sides are given
a = float(input("Enter side a of the triangle: "))
b = float(input("Enter side b of the triangle: "))
c = float(input("Enter side c of the triangle: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle is: {area}")
