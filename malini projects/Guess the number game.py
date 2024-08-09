import random
a = random.randint(10, 100)
print("Welcome to the Guessing number world!!!\n"
      "Here you have 3 attempts and \n"
      "Think a number between 10 to 100")
print(30*'*')
x=3
for i in range (1,4):
    b = int(input('enter a value:'))
    if a!=b:
        x-=1
        print("you are wrong still you have", x, 'attempts')
    else:
        print("Congratulations, you won!\n And the number is ")
print("The Random number is :",a)