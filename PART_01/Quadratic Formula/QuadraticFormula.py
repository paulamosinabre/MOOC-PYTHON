from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

squ = sqrt((b * b) - 4 * a * c)
pos = (-b + squ) / (2*a)
neg = (-b - squ) / (2*a)

print(f"The roots are {pos} and {neg}")
