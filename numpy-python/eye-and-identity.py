# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy

# there is an error on the code setters part and tehe below cde although absolutely correct doesn't pass the test cases
M, N = map(int, input().split())
# print(numpy.eye(M, N))

# The problem setter's code prints 1's and 0's with an extra space and hence we will add an extra space in front of
# 0 and 1 using replace() function

print(str(numpy.eye(M, N)).replace('1',' 1').replace('0',' 0'))
