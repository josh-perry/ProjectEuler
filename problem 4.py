# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def check_palindrome(n):
	s = str(n)

	# Get left side of string
	s_left = s[:len(s)/2]

	# Get right side of string
	s_right = s[len(s)/2:]

	# Flip right side
	s_right = s_right[::-1]

	if s_left == s_right:
		return True
	
	return False


def euler_4():
	products = set()

	for i in range(100, 999 + 1):
		for j in range(100, 999 + 1):
			products.add(i * j)

	palindromes = []
	for i in products:
		if check_palindrome(i):
			palindromes.append(i)

	print("The answer should be: " + str(max(palindromes)))

if __name__ == "__main__":
	euler_4()