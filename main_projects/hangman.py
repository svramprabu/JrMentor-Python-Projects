# guess the word
# Step 1 computer assumes a word
import random
list_of_words = ['python','programming','hackerkid']
com = random.choice(list_of_words)
guess = []
word_on_screen = ''
attempts = len(com)+2

while(attempts > 0):
    # step 2 resultant word with dashes
    word_on_screen = ''
    for each_letter in com:
        if each_letter in guess:
            word_on_screen += each_letter
        else:
            word_on_screen += '_'
    print(word_on_screen)

    # step 5 closing with success
    if word_on_screen == com:
        print('You found the answer')
        break

    # step 3 get user input for a letter
    print(f'you have {attempts} attempts left')
    user_input = input('Choose a possible letter: ').lower()
    if user_input in com:
        print(user_input,'is in the word')
    else:
        print(user_input,'is not in the word')
    # step 4
    if user_input in guess:
        print('but you tried the letter before')
    else:
        attempts -= 1
        guess.append(user_input)

# step 6 after coming out of while loop
if attempts == 0:
    if word_on_screen == com:
        print('You found the word')
    else:
        print('Try again later')