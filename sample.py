import numpy as np


#numpy.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)

EX = np.array([[1,2,3],[4,5,6]])
print("Ex",EX)
print("Ex",EX.shape)
#print(n.size())

#ndim
Ex1=np.array([1,2,3,4,5,6,7,8,9],ndmin=2)
print("Ex1",Ex1)
print("Ex1",Ex1.shape)

#dtype

EX2=np.array([1,2,3,4,5,6],dtype=complex)
print("Ex2",EX2)
print("Ex2",EX2.shape)

#dtype

EX3=np.array([1,2,3,4,5,6],dtype=long)
print("Ex3",EX3)
print("Ex3",EX3.shape)


