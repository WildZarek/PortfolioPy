# Count Words in a Sentence with Python.
# by WildZarek ~ 2024

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <string>")
    else:
        txt = sys.argv[1]
        if txt:
            words = txt.split()
            if words:
                longest_word = max(words, key=len)
                print(f"The number of words in the sentence is: {len(words)}")
                print(f"The longest word in the sentence is: '{longest_word}'")
        else:
            print("The input string is empty.")