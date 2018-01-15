import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a)

print ('Now we will slice the array from the index a[1:]')
print (a[1:])

print (a[...,1])
print ('\n')
print (a[1,...])
print ('\n')