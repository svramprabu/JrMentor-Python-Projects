def main():
    while True:
        option = input("+ or - or * or / : ")
        if option == '+':
            add()
        elif option == '-':
            a = int(input('a='))
            b = int(input('b='))
            print(sub(a,b))
def add():
    a = int(input('a='))
    b = int(input('b='))
    result = a+b
    print(f"Addition answer: {result}")
def sub(a,b):
    result = a-b
    return f"Subtraction answer: {result}"

main()