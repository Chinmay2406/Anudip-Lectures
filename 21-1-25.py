 """Fixed word
word = "swiss"
 Create a frequency dictionary
char_count = {}

Count the occurrences of each character
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

 Find the first character with a count of 1
for char in word:
    if char_count[char] == 1:
        print("First non-repeating alphabet:", char)
        break
else:
    print("No non-repeating alphabet found.")"""

str = "swiss"
for char in str:
    if str.count(char) == 1:
        print(f" first non-repeating char is: {char}")
        break
else:
    print("No non-repeating chat in str.")
