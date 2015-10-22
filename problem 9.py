# coding=utf8

# Problem 9: Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math


def euler_9():
    product_found = False
    n = 1000

    for a in range(1, n/2):
        for b in range(1, n/2):
            c = (n-a-b)

            a2 = a**2
            b2 = b**2
            c2 = c**2

            if a2 + b2 == c2:
                product_found = True
                print("Found the product: " + str(a*b*c))
                return


if __name__ == "__main__":
    euler_9()
