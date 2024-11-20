def main():
    while True:
        option = input('\n+ - * / \nyour option: ')
        if (option == '+'):
            add()
        elif (option == '-'):
            print(subtract())
        elif (option == '*'):
            a = int(input('a='))
            b = int(input('b='))
            multiply(a,b)
        elif (option == '/'):
            a = int(input('a='))
            b = int(input('b='))
            print(divide(a,b))
        else:
            print('Invalid option')
            break
def add():
    a = int(input('a='))
    b = int(input('b='))
    print(f"{a}+{b}={a+b}")
def subtract():
    a = int(input('a='))
    b = int(input('b='))
    return f"{a}-{b}={a - b}"
def multiply(a,b):
    print(f"{a}*{b}={a * b}")
def divide(a,b):
    return f"{a}/{b}={a / b}"

if __name__ == '__main__':
    main()