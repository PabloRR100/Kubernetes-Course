

import numpy as np 

x = np.random.randn(10)
y = np.random.randn(5,10)

np.sum(y * x, axis=1)
np.dot(y,x)