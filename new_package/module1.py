# print('Hi form module 1')
def add(): #type 1 no argument & no return value
    a = int(input('a='))
    b = int(input('b='))
    print(f'{a}+{b}={a+b}')

def sub(): #type 2 no argument with return value
    a = int(input('a='))
    b = int(input('b='))
    return f"{a}-{b}={a - b}"

def mul(a,b): #type 3 with argument and no return
    print(f"{a}x{b}={a*b}")

def div(a,b): #type 4 with argument and return value
    return f"{a}/{b}={a/b}"