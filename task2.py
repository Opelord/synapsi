import random

minimum = 20
maximum = 150


def read_number():
    try:
        y = int(input(f"Input number in range {minimum} - {maximum}: "))
    except Exception as e:
        print(f"Could not read with error: {e}")
        return None
    return y


x = read_number()
while x is None or not minimum <= x <= maximum:
    print("Incorrect input!")
    x = read_number()

print("Thank you!")
