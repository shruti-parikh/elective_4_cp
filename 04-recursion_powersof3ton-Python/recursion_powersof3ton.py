# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def rec(n, power=0, L = None):
	if L == None:
		L = []
	if power == 0:
		L.append(1)
	if n < 1:
		return None
	else:
		power = power + 1
		next = 3 ** power
		if(next > n):
			return L
		L.append(next)
		return rec(n, power, L)

def recursion_powersof3ton(n):
	return rec(n)


	# Your code goes here
	
