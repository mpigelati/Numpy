import numpy as np

a = np.asarray(2)
print(a)

x=np.asarray([1,2,3])
print(x)

array=[1,2,3]

b = np.asarray(array)

print("asarray",b)

c = np.asarray(array,dtype=float)

print(c)

d = np.asarray(array,dtype=int)
print(d)


b_array=[(1,2,3),(4,5,6)]

b_np = np.asarray(b_array)

print(b_np)