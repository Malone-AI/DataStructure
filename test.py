import numpy as np

def change(array):
    array[0][0]=-1

x=np.array([[0,1],[0,0]])

print(x)
change(x)
print(x)
