# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	n = len(l)
	alter_sum = 0
	for i in range(n):
		if i %2 == 0:
			alter_sum += l[i]
		elif i%2 != 0:
			alter_sum -= l[i]
	return alter_sum


