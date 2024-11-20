import random
chosen_number = random.randint(1,100)
user_number = int(input('Guess the number: '))
while True:
    if user_number == chosen_number:
        print('Congratsss you found the number',chosen_number)
        break
    elif user_number > chosen_number:
        user_number = int(input('Please enter a smaller no: '))
    elif user_number < chosen_number:
        user_number = int(input('Please enter a bigger no: '))
