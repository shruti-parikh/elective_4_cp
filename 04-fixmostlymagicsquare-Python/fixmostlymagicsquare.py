# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# Your code goes here
	n = len(L)
	r = 0
	c = 0
	num = 0
	if n == 1:
		return True
	for i in range(n):
		for j in range(n):
			r = r + L[i][j]
			c = c + L[j][i]
		if r!= c and num == 0:
			num = 1
			L[i][j] = L[i][j]-(r-c)
	return L

