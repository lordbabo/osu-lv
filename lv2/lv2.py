# Primjer 2.1
import numpy as np
a = np.array([6, 2, 9]) 
print(type(a)) 
print(a. shape ) 
print(a[0], a[1], a[2]) 
a[1] = 5 
print(a) 
print(a[1:2]) 
print(a[1:-1]) 
b = np.array([[3,7,1],[4,5,6]]) 
print(b.shape) 
print(b) 
print(b[0, 2], b[0, 1], b[1, 1]) 
print(b[0:2,0:1]) 
print(b[:,0]) 
c = np.zeros((4,2)) 
d = np.ones((3,2)) 
e = np.full((1,2),5) 
f = np.eye(2) 
g = np.array([1, 2, 3], np.float32 )
duljina = len(g)
print(duljina)
h = g.tolist()
print(h)
c = g.transpose()
print(g)
np.concatenate((a, g ,))