# Simple Dice Rolling Simulator.
# by WildZarek ~ 2024

import random

def roll_a_dice() -> int:
    return random.randrange(1, 7)

if __name__ == "__main__":
    print(f"You rolled a {roll_a_dice()}!")