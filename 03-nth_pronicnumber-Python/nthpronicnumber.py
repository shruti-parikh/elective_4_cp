# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronicnumber(n):
	# Your code goes here
	for i in range(n):
		if i * (i +1) == n:
			return True
	return False

def nthpronicnumber(n):
	i = 1
	j = 0
	while i <= n:
		j += 1
		if pronicnumber(j):
			i += 1
	return j
			
	