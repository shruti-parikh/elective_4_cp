# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	digitcount = [0]*10
	st = str(n)
	max_count = 0
	res = 0
	for i in st:
		digitcount[int(i)]+= 1
	for num, count in enumerate(digitcount):
		if count > max_count:
			max_count = count
			res = num
	return res


		