import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print(roll_dice())

if __name__ == '__main__':
    main()
