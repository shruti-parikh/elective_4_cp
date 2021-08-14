# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	if len(a) == 0:
		return []
	lst = []
	count = 1
	j = 0
	i = 0                    
	# 1 1 2 2 1 1 1 i = 0 --> count = 2; i = 2 --> count 2; 
	while ( i < len(a)) :
		while ( i+1 < len(a) and a[i] == a[i+1]) :
			i += 1
			count += 1
		lst.insert(j , (count , a[i]))
		count = 1
		j+=1
		i += 1
	return lst 
	
	