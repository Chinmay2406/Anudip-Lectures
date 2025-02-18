"""import sys
def generate_num(n):
    i=1
    while i<=n:
       yield i 
       i += 1

   
gen = generate_num(100)
for num in gen:
    print(num, end="")

print()
size = sys.getsizeof(gen)
print(size)  #192 """


"""new_list = list(range(1,1000))
print(new_list)

size = sys.getsizeof(new_list)
print(size)
"""
#gen and iterator
"""import sys
def generate_num(n):
    i=1
    while i<=n:
        yield i
        i +=1

gen = generate_num(100)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(list(gen))"""

#fibonacci series without generator
"""def fibonacci(n):
    a, b = 0, 1 
    for i in range(n):
        print(a, end=" ")  
        a, b = b, a + b  
fibonacci(10)"""


#fibonacci series with generator
"""def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_generator(8):
    print(num, end=" ")"""

#generating squares

"""print("=====Generating squares using list comprehension=====")
squares = [num**2 for num in range(1,6) ]
print(squares)

print("=====Generating squares using generators=====")
squares = (num**2 for num in range(1,6))
print(squares)

squares = (num**2 for num in range(1,6))
for sq in squares:""
    print(sq, end="")"""

