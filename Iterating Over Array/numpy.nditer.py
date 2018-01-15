import  numpy as np

a=np.arange(0,60,5)
print(a)
print(a.shape,"\n")

a= a.reshape(3,4)
print(a)
print(a.shape,"\n")

b=a.T
print("b",b)

for i in np.nditer(b):
    print(i)
