# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = dict()
	for each in s:
		if each not in d:
			d[each] = 1
		else:
			d[each] += 1
	count = sorted(d.values(), reverse = True)[n-1]
	for key in d:
		if d[key] == count:
			return key
	
	
	 
		



