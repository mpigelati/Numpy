import numpy as np

dt= np.dtype(np.int32)
print (dt)

dt= np.dtype('i1')
print (dt)
dt= np.dtype('i2')
print (dt)
#dt= np.dtype('i3')
#print (dt)
dt= np.dtype('i4')
print (dt)
#dt= np.dtype('i5')
#print (dt)


dt= np.dtype=(["age",np.int])
print (dt)

dt= np.dtype=(["age",np.int],)
print (dt)

#dt=np.dtype([('age',np.int8)])
#a=np.array([10,20,30,40,50,60],dtype=dt)
#print (a)
#dt=np.dtype([('age',np.int8)])
#a=np.array([(10,),(20,),(30,)], dtype=dt)
#print (a.age)

dt=np.dtype('i4')
print(dt)