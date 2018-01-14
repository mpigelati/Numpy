import numpy as np




x=np.zeros(5)
print(x)

y=np.zeros((5),dtype=int)
print(y)

print('\n')
z=np.zeros((5),dtype=float)
print(z)
print('\n')
a=np.zeros((2,2),dtype=[('x',"i4"),('y','i4')])
print(a)
print('\n')
b=np.zeros((2,2),dtype= int)
print(b)


c = np.ones((2,2),dtype=int)
print(c)

d=np.ones((2,2),dtype=[('x',"i4"),('y','i4')])
print(d)
