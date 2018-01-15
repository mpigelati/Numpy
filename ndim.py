import numpy as np

#EX= np.array([[1,2,3],[4,5,6,],[7,8,9]])
#print(EX)

a = np.arange(24)
print(a)


b= a.reshape(12,2)
print(b)

print('\n   ')
c = a.reshape(2,4,3)
print(c)
