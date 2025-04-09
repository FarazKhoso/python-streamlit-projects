# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    print(f"total = {total}")

def main():
    die1 = 10
    print(f"die1 trynit first time {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 trynit last time {die1}")

main()