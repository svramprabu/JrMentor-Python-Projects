def main():
    sides = int(input('Enter sides: '))
    print('After rolling we got ',dice_roll(sides))

def dice_roll(sides=6):
    import random
    dice = random.randint(1,sides)
    return dice

if __name__ == '__main__':
    main()