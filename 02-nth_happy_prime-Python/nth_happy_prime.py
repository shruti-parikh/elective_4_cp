# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
def isprime(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	for i in range(3, int(n**0.5)+1, 2):
		if n%i==0:
			return False    
	return True
def square(n):
	sum = 0
	while n > 0:
		r = n%10
		sum += r*r
		n = n//10
	return sum
def ishappy(n):
	while n >= 10:
		n = square(n)
		if n == 1:
			return True
	return False

def fun_nth_happy_prime(n):
	count = 0
	if n == 0:
		return 7
	num= 7
	while True:
		if isprime(num) and ishappy(num):
			count+= 1
		if count == n:
			return num
		num += 1


	