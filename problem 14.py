# coding=utf8

# Problem 14: Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def n_even(n):
    return n / 2


def n_odd(n):
    return (n * 3) + 1


def euler_14():
    biggest_chain = 0
    biggest_chain_n = 0

    for starting_n in xrange(1, 1000000):
        n = starting_n
        chain = 0

        while not n == 1:
            if n % 2 == 0:
                n = n_even(n)
            else:
                n = n_odd(n)

            chain += 1

        if chain > biggest_chain:
            biggest_chain = chain
            biggest_chain_n = starting_n

    print("Biggest chain: " + str(biggest_chain))
    print("The answer should be: " + str(biggest_chain_n))


if __name__ == '__main__':
    euler_14()
