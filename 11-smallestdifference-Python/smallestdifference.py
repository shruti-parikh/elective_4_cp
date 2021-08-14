# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if len(a) == 0:
		return -1
	a.sort()
	minDiff = a[1]-a[0]
	i = 2
	while i != len(a):
		minDiff = min(minDiff, a[i]- a[i-1])
		i += 1
	return minDiff
