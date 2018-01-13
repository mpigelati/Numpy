import numpy as np

''' shape should to nultiplease for arrar
3x2 ([1,2,3],[4,5,6,])
'''

EX= np.array([[1,2,3],[4,5,6,],[7,8,9]])
print(EX)
print(np.shape(EX))

EX1= np.array([[1,2,3],[4,5,6,]])
RE_EX1= EX1.reshape(3,2)
print(RE_EX1)

EX2= np.array([[1,2,3],[4,5,6,],[7,8,9]])
RE_EX2= EX2.reshape(9,1)
print(RE_EX2)
RE_EX3= EX2.reshape(1,9)
print(RE_EX3)