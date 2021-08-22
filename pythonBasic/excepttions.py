from os import error
import sys
try:
    x = int(input("Input x: "))
    y = int(input("Input y: "))
except ValueError:
    print("Wrong input")
    sys.exit(1)

try:
    result = x/y
    print(f"{x}/{y} = {result}")
except ZeroDivisionError:
    print("Zero Division")
    sys.exit(1)
