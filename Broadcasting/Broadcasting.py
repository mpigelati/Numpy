import  numpy as np

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.shape)


x= np.array([10,20,30,40,50])

y= np.array([60,70,80,90,100])

z= x*y
print(z)


b= np.array([1,2,3])
c= a*b
print(c)

print("\n")
d= np.array([[1,2,3],[4,5,6],[7,8,9]])
e = b*d
print("e",e)
