import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print(a)

print(a.ndim)

print(a.itemsize)

b=np.array([1,2,3,4,5])

print(b.itemsize)


c=np.array([1,2,3,4,5],dtype=np.int8)
print(c.itemsize)

d=np.array([1,2,3,4,5],dtype=np.int32)
print(d.itemsize)

e=np.array([1,2,3,4,5],dtype=np.int64)
print(e.itemsize)

#f=np.array([1,2,3,4,5],dtype=np.int128)
#print(f.itemsize)

g=np.array([1,2,3,4,5],dtype=np.uint64)
print("unint",g.itemsize)

h=np.array([1,2,3,4,5],dtype=np.float64)
print("float",h.itemsize)