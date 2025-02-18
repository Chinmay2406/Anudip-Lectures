str = "swiss"
for char in str:
    if str.count(char) == 1:
        print(f" first non-repeating char is: {char}")
        break
else:
    print("No non-repeating chat in str.")