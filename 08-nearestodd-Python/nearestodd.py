# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.


import math 
def fun_nearestodd(n):
	n = str(n)
	x, y = n.split('.')
	x = int(x)
	y = int(y)
	if x%2 == 0 and y== 0:
		return x-1
	elif x%2 == 0 and int(y) > 0:
		return x+1
	else:
		return x
		


