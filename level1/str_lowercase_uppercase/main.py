# Algorithm to count Uppercase and Lowercase letters in a given String.
# by WildZarek ~ 2024

import sys

def count_upper_lower(txt: str = "") -> tuple:
    if txt != "":
        count_upper = sum(1 for char in txt if char.isupper())
        count_lower = sum(1 for char in txt if char.islower())
        return count_upper, count_lower

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <string>")
    else:
        txt = sys.argv[1]
        if txt:
            upper_lower = count_upper_lower(txt)
            print(f"The number of uppercase letters in the string is: {upper_lower[0]}")
            print(f"The number of lowercase letters in the string is: {upper_lower[1]}")
        else:
            print("The input string is empty.")