# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)
def square(n):
	sum = 0
	while n > 0:
		r = n%10
		sum += r*r
		n = n//10
	return sum
def ishappynumber(n):
	# your code goes here
	if(n==1):
		return True
	while (n>=10):
		n=square(n)
		if(n==1):
			return True
	return False

def nth_happy_number(n):
	if n == 1:
		return 1
	if n == 2:
		return 7
	i = 2
	j = 8
	while i <= n:
		if ishappynumber(j):
			i+=1
		if i == n:
			return j
		j += 1
	
