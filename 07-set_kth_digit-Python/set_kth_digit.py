# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def length(n):
    x = str(n)
    return len(x)

def fun_set_kth_digit(n, d, k):

	# rev = n%10**(d+1)
	# if length(rev) == 1:
	# 	return  n - rev + k 
	# elif length(n) == d:
	# 	x = k*10**d
	# 	return x+n
	# else:
	# 	l = length(rev)
	# 	d = l
	# 	sub = (rev%10**(d))
	# 	while d-1 > 0:
	# 		sub -= (rev%10**(d-1))
	# 		d = d -1
	# 	n = n - sub
	# 	x = k * 10**(d)
	# 	return n+x
	if n == abs(n):
		n_str = str(n)[::-1]
		new = n_str[:d] + str(k) + n_str[d+1:]
		return int(new[::-1])
	else:
		n_str = str(abs(n))[::-1]
		new = n_str[:d] + str(k) + n_str[d+1:]
		return -int(new[::-1])





	



		

