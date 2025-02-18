# 20-1-25
#REGEX

"""
text = "chinmay.deshmukh@gmail.com"
pattern = r"."
search = re.search(pattern,text)
print(search) 
#  <re.Match object; span=(0, 1), match='c'>


text = "chinmay.deshmukh@gmail.com"
pattern = r"."
search = re.search(pattern,text)
print(search) 

<re.Match object; span=(7, 8), match='.'> 

import re

text = "chinmay.deshmukh203@gmail.com"
pattern = r"\bchinmay\b"
search = re.findall(pattern,text)
print(search) 


import re

text = "10 * 8 = 80"
pattern = r"10 * 8"
search = re.search(pattern,text)
if search:
    print("match found") 
else:
    print("Match not found")

import re

text = "Hello, I am chinmay deshmukh 9383783 and 7726728 and 6624526"
pattern = r"d+"
match = re.finditer(pattern,text)

for num in match:
    print(num)
    print(num.start(), num.end())


import re

text = "Hello, I am chinmay deshmukh 9383783 and 7726728 and 6624526"
pattern = r"d"
replaced_text = re.sub(pattern, "*", text)
print(replaced_text)"""

#metacharacters
import re
pattern = r"arun|varun"
text = "arun, tarun, varun"
matches = re.findall(pattern, text)
print(matches)

