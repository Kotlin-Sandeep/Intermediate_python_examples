import numpy as np

A = np.mat("0,1,2;1,0,3;4,5,6")
print("Value of matrix A \n",A)

B = np.mat("10,11,12;11,10,13;14,15,16")
print("Value of matrix B \n",B)

C = A.dot(B)
print("Result is: \n", C)
