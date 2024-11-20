def rps():
    print('Welcome to my Rock Paper Scissors Game')
    p1 = input('Choose Rock(r) or Paper(p) or Scissors(s): ').lower()[0]
    p2 = input('Choose Rock(r) or Paper(p) or Scissors(s): ').lower()[0]

    if (p1 == 'r' and p2 == 'p'):
        print('player 2 won')
    elif (p1 == 'p' and p2 == 'r'):
        print('plauer 1 won')
    elif (p1 == 'p' and p2 == 's'):
        print('plauer 2 won')
    elif (p1 == 's' and p2 == 'p'):
        print('plauer 1 won')
    elif (p1 == 's' and p2 == 'r'):
        print('plauer 2 won')
    elif (p1 == 'r' and p2 == 's'):
        print('plauer 1 won')
    elif (p1 == p2):
        print('Its a tie')
    else:
        print('Invalid input')

while True:
    rps()