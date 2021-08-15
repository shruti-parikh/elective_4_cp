# Background: we can represent a polynomial as a list of its coefficients. 
# For example, [2, 3, 0, 4] could represent the polynomial 2x3 + 3x2 + 4. 
# Write the function multiplyPolynomials(p1, p2) which takes two polynomials 
# and returns a third polynomial which is the product of the two. For example,
# multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 5), and:
# (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns [8, 10, 12, 15].

def multiplyPolynomials(p1, p2):
    # Your code goes here...
    m = len(p1)
    n = len(p2)
    prod = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            prod[i + j] += p1[i] * p2[j]
    return prod

# Write your own test cases
print(multiplyPolynomials([2,0,3], [4,5]))
print ("All test cases passwed...")