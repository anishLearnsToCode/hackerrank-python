# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

array = np.array(list(map(int, input().split())))
array.shape = (3, 3)
print(array)
