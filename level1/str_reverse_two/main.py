# Two different algorithms to reverse a given String.
# by WildZarek ~ 2024

import sys

def str_reverse_1(txt: str = "") -> str:
    if txt != "":
        reversed_str = ""
        for char in txt:
            reversed_str = char + reversed_str
        return reversed_str
    # We can reduce this to one-line:
    # return "".join(txt[i] for i in range(len(txt)-1, -1, -1))

def str_reverse_2(txt: str = "") -> str:
    if txt != "":
        reversed_str = txt[::-1]
        return reversed_str

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <string>")
    else:
        txt = sys.argv[1]
        if txt:
            print(f"(Method 1) The reversed string is: {str_reverse_1(txt)}")
            print(f"(Method 2) The reversed string is: {str_reverse_2(txt)}")
        else:
            print("The input string is empty.")