# Background: a Kaprekar number is a non-negative integer, the representation of whose sqr_numuare 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def kaprekar(n):
    if n==1:
        return True
    sqr_num = n*n
    count = len(str(sqr_num))
    d = 0
    while(d < count):
        d = d + 1
        eq_parts = int(math.pow(10,d))
        if eq_parts == n :
            continue
        sum = (sqr_num//eq_parts) + (sqr_num % eq_parts)
        if sum == n :
            return True
    return False

def fun_nth_kaprekarnumber(n):
    lis = []
    i = 1
    j = 0
    while(j<=n):
        if(kaprekar(i)==True):
            j = j + 1
            lis.append(i)
        i = i+1
    return lis[n]