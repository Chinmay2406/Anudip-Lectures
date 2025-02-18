# Program 5: Calculate fare based on distance
distance = float(input("Enter the distance traveled (in km): "))

if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = distance * 10
elif distance > 100:
    fare = distance * 12
else:
    print("Invalid distance!")
    fare = 0

print(f"The total fare is Rs. {fare:.2f}.")
