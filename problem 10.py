# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


import math


# Same function as problem 3
def is_prime(n):
    maximum = int(math.sqrt(n) + 1)

    if n == 1 or n == 0:
        return False

    for i in range(2, maximum):
        if n == 1 or (n % i == 0 and i != n):
            return False

    return True


def euler_10():
    big_number = 2000000
    sieve = [True] * big_number

    for n in xrange(2, big_number):
        if not sieve[n]:
            continue

        if not is_prime(n):
            sieve[n] = False

        for i in xrange(n+n, len(sieve), n):
            sieve[i] = False

    # Compensate for 1 not being checked
    total = -1
    for x in range(1, len(sieve)):
        if sieve[x]:
            total += x

    print total


if __name__ == "__main__":
    euler_10()
