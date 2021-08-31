# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def prime(n):
    if(n < 2):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def sumdigits(n):
    s = 0
    while(n > 0):
        s = s + (n % 10)
        n = n // 10
    return s
def primefact(n):
    i = 2
    s = 0
    l = []
    while(i*i <= n):
        if(n % i == 0):
            s = s + sumdigits(i)
            l.append(i)
            n = n // i
        else:
            i = i + 1
    if(n > 1):
        l.append(n)
        s = s + sumdigits(n)
    return s

def smith(n):
    if(prime(n)):
        return False
    if(sumdigits(n) == primefact(n)):
        return True
    return False


def fun_nth_smithnumber(n):
    c = 0
    i = 0
    while(c <= n):
        i = i+ 1
        if(smith(i)):
            c = c+ 1
    return i