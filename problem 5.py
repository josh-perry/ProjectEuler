# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?


def check_div(n):
    # Don't bother checking 20, we're iterating n by 20 anyway
    for i in range(11, 19 + 1):
        if n % i != 0:
            return False

    return True


def euler_5():
    n = 0

    while True:
        n += 20

        if check_div(n):
            print("The correct answer should be: " + str(n))
            break


if __name__ == "__main__":
    euler_5()
