# Python program to find the area of a triangle whose sides are given
a = float(input())
b = float(input())
c = float(input())

# Check if the triangle inequality theorem is satisfied
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Using exponentiation for square root
    print(area)
else:
    print("Invalid triangle sides")
