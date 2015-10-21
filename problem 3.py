# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def is_prime(n):
    maximum = int(math.sqrt(n) + 1)

    if n == 1:
        return False

    for i in range(2, maximum):
        if n == 1 or (n % i == 0 and i != n):
            return False

    return True


def euler_3(big_number=13195):
    maximum = int(math.sqrt(big_number) + 1)

    prime_factors = []

    for i in range(1, maximum):
        if is_prime(i) and big_number % i == 0:
       		prime_factors.append(i)

    print("The answer should be: " + str(max(prime_factors)))


if __name__ == "__main__":
    euler_3(600851475143)
