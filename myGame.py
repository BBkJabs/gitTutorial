import random
import os

def roll_dice():
    return random.randint(1, 6)

def main():
    welcomeMessage()
    print(roll_dice())

def welcomeMessage():
    os.system('cls' if os.name=="nt" else 'clear')
    print("Game 'Pig'")
    print("=================")
    print("Welcome to the push-your-luck game Pig!")
    print("This is a die game for 2-4 players.")
    print("The game is played over several rounds.")
    print("In each round, players may roll a die.")
    print("If a player rolls a 1, they score no points for the round and it becomes the next player's turn.")
    print("If a player rolls a 2-6, they can either hold (stop rolling) or roll again.")
    print("If they hold, they score the sum of the rolls during the round.")
    print("The first player to score 100 or more points wins the game.")
    print("Good luck!")

if __name__ == '__main__':
    print(random.randint(1, 6))
