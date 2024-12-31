# Check if Number is Positive or Negative Using Function 
# by WildZarek ~ 2024

import sys

def check_number(number: float) -> str:
    if number.is_integer():
        number = int(number)
    if number > 0:
        return f"The number {number} is positive."
    elif number < 0:
        return f"The number {number} is negative."
    else:
        return f"The number {number} is zero."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <number>")
    else:
        try:
            number = float(sys.argv[1].replace(',', '.'))
            print(f"Input number: {sys.argv[1]}")
            print(check_number(number))
        except ValueError:
            print("The input is not a number.")