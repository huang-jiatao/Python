import numpy as np

a = np.arange(15).reshape(3, 5)
b = np.ones((3, 5)) * 3
'''
a = np.array([1, 2, 3], dtype=np.float64)
a = np.linspace(0, 1, 11)
a = np.zeros((3, 5))
a = np.ones((3, 3)) * 3
a = np.eye(3)
a = np.diag([1, 2, 3]) * 2

print(a.dtype)
b = a[:2, 1::2]
'''
print(a)
print(b)
#c = a < b
c = np.sum(a)
print(a.sum(axis=1))
print(c)

print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)
