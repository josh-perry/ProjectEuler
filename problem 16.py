# coding=utf8

# Problem 16: Power digit sum
# 2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2¹⁰⁰⁰?


def euler_16():
    total = 0

    for c in str(2**1000):
        total += int(c)

    print("The answer should be: " + str(total))


if __name__ == '__main__':
    euler_16()
