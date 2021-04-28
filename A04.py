# Python Programming - Sections 1811
# Programming Assignment 4
# Instructor: Dr. Scott Bishop
# Student: Vladimir Palenov

# Program 1:  Computing the Prefix Sum
# def prefixsum(A):
# This function takes in a 1D numerical list
# and returns a  new  list  where  each  entry
# is  computed  by  adding  adjacent elements
# of  the  input  list.
def prefixsum(A):
    result = []
    current = 0
    for elem in range(len(A)):
        current = current + A[elem]
        result.append(current)
    return result

# Testing Program 1.
test1 =  [0,-10,10,20,-20,100]
print(prefixsum(test1)) #expected result [0,  -10, 0, 20, 0, 100]

# Program 2:  Matrix (2D List) Symmetry
# def symmetric(m):
# function accepts one argument, a matrix m, and returns true
# if the matrix is symmetric or false otherwise.
def symmetric(m):
    result = True
    for a in range(len(m)):
        for b in range(len(m[a])):
            if (m[a][b] != m[b][a]):
                result = False
    return result
# Testing Program 2.
m1 = [[3, 5, 9], [5, 7, 1], [9, 1, 5]]
m2 = [[3, 5, 10], [5, 0, 6], [10, 7, 1]]
m3 = [[0, 0], [0, 0]]
print(symmetric(m1)) #True
print(symmetric(m2)) #False
print(symmetric(m3)) #True

# Program 3:  The Transpose of a Matrix (2D List)
# def transpose(m):
# function accepts one argument, a matrix m, and returns
# the transpose matrix. The original matrix is not modified.
def transpose(m):
    result = []
    for c in range (len(m[0])):
        inner = []
        for d in m:
            inner.append(d[c])
        result.append(inner)
    return result
# Testing Program 3.
m5 = [[1, 2, 3, 4], [5, 6, 7, 8]]
m6 = [[1, 2, 3, 4]]
m7 = [[1, 2], [3, 4], [5, 6]]
print(transpose(m5)) #expected [[1, 5], [2, 6], [3, 7], [4, 8]]
print(transpose(m6)) #expected [[1], [2], [3], [4]]
print(transpose(m7)) #expected [[1, 3, 5], [2, 4, 6]]
