# Check if Number is Positive or Negative
# by WildZarek ~ 2024

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <number>")
    else:
        try:
            input_value = sys.argv[1].replace(',', '.')
            number = float(input_value)
            if number < 0:
                result = "negative"
            elif number == 0:
                result = "zero"
            else:
                result = "positive"
            print(f"Input number: {sys.argv[1]}")
            print(f"The number is {result}.")
        except ValueError:
            print("The input is not a number.")