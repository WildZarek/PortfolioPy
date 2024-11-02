# Algorithm to count Vowels and Consonants in a given String.
# by WildZarek ~ 2024

import sys

def count_vowels_consonants(txt: str = "") -> tuple:
    if txt != "":
        vowels = set("aeiou")
        consonants = set("bcdfghjklmnpqrstvwxyz")
        count_vowels = sum(1 for char in txt.lower() if char in vowels)
        count_consonants = sum(1 for char in txt.lower() if char in consonants)
        return count_vowels, count_consonants

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <string>")
    else:
        txt = sys.argv[1]
        if txt:
            vowels_consonants = count_vowels_consonants(txt)
            print(f"The number of Vowels in the string is: {vowels_consonants[0]}")
            print(f"The number of Consonants in the string is: {vowels_consonants[1]}")
        else:
            print("The input string is empty.")