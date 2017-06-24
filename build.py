import numpy as np



def solution(array):
    """
    Enter your code here
    """
    carray=[]
    for i in array:
        carray.append((i-32)*(5.0/9))
    mat=np.array(carray)
    return mat
