# islegaltriangle(s1, s2, s3)
# Write the function islegaltriangle(s1, s2, s3) that takes three int or float values representing
# the lengths of the sides of a triangle, and returns True if such a triangle exists and False
# otherwise. Note from the triangle inequality that the sum of each two sides must be greater
# than the third side, and further note that all sides of a legal triangle must be positive. Hint:
# how can you determine the longest side, and how might that help?

def islegaltriangle(a, b, c):
	# your code goes here
	if (a + b <= c) or (a + c <= b) or (b + c <= a) :
		return False
	else:
		return True 
