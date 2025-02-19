def main():
    while True:
        option = input('+ - * /: ')
        if option == '+':
            addition()

def addition(): #type 1
    a = int(input('a='))
    b = int(input('b='))
    print(a,'+',b,'=',a+b)

main()