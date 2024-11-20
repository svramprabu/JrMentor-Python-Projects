def main():
    print('Welcome to my calculator app')
    while True:
        option = input('+ - * /'
                       '\nyour option:')
        if option == '+':
            add() #type 1 
        elif option == '-':
            print(sub()) #type 2
        elif option == '*':
            print('Multiplication')
            a = int(input('a='))
            b = int(input('b='))
            mul(a,b) #type 3
        elif option == '/':
            print('Division')
            a = int(input('a='))
            b = int(input('b='))
            print(div(a,b))
        else:
            print('invalid input')
def add():
    print('Addition')
    a = int(input('a='))
    b = int(input('b='))
    print(f'{a}+{b}={a+b}')
def sub():
    print('Subtraction')
    a = int(input('a='))
    b = int(input('b='))
    return f'{a}-{b}={a-b}'
def mul(a,b):
    print(f'{a}*{b}={a*b}')
def div(a,b):
    return f'{a}/{b}={a/b}'

if __name__ == '__main__':
    main()