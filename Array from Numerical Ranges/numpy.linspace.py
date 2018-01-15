import numpy as np
x = np.linspace(10,20,5)
print(x)

x = np.linspace(10,20, 5, endpoint=False)
print (x)

x = np.linspace(1,2,5, retstep=True)
print (x)
