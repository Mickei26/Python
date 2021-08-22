import func
from func import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# cach 2 de import function

for i in range(10):
    print(f"The square of {i} is {func.square(i)}")
