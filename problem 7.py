# Problem 7: 10001st Prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


import math


# Same function as problem 3
def is_prime(n):
    maximum = int(math.sqrt(n) + 1)

    if n == 1:
        return False

    for i in range(2, maximum):
        if n == 1 or (n % i == 0 and i != n):
            return False

    return True


def euler_7():
	n = 1
	prime_count = 0

	while prime_count < 10001:
		n += 1

		if is_prime(n):
			prime_count += 1

	print("The answer should be: " + str(n))


if __name__ == "__main__":
	euler_7()