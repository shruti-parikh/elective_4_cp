# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
def permutation(a,ans,lis):
	if len(a) == 0:
		fin_lis = []
		for i in ans:
			fin_lis.append(i)
		t = tuple(fin_lis)
		lis.append(t)
	for i in range(len(a)):
		ch = a[i]
		l_str = a[0:i]
		r_str = a[i+1:]
		res = l_str + r_str
		permutation(res,ans+ch,lis)
	return lis

def getallpermutations(x):
	# Your code goes here
	ans = ""
	return permutation(x,ans,lis=[])
