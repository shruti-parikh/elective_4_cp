# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    n = len(lst)
    rows = []
    row = 0
    col = 0
    v = 0
    for i in range(n):
        rows.append(set([]))
    cols = []
    for i in range(n):
        cols.append(set([]))
    for i in range(n):
        for j in range(n):
            rows[i].add(lst[i][j])
            cols[j].add(lst[i][j])
            if (lst[i][j] > n or lst[i][j] <= 0):
                v = v + 1
    for i in range(n):
        if (len(rows[i]) != n):
            row = row + 1
        if (len(cols[i]) != n):
            col = col + 1
    if (col == 0 and row == 0 and v == 0):
        return True
    else:
        return False
