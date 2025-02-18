"""def fib(n):
    i = 1
    a,b = 0,1
    for i in range(n):
        print(a, end=" ")
        a,b = b,a+b
        i+=1

fib(10)"""


def fib(n):
    i = 1
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b
        

for num in fib(10):
    print(num, end=" ")



















