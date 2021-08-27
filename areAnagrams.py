# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    s1=s1.lower()
    s2=s2.lower()

    lis = [0]*26
    for each in s1:
        index = ord(each) - ord('a')
        lis[index] += 1
    for each in s2:
        count =  ord(each) - ord('a')
        lis[count] -= 1
    if sum(lis) == 0:
        return True
    else:
        return False



# write your test cases here...
assert(areAnagrams('Acsa','scaa') == True)
assert(areAnagrams('ASEDFR','asedrf') == True)
assert(areAnagrams('kwswki','ikswwk') == True)
assert(areAnagrams('Aswdr','asdf') == False)
assert(areAnagrams('hyuj','hnukn') == False)
print("All test cases passed... :-)")