import numpy as np



def solution(arr):
    list_f = np.array(arr)
    return (list_f - 32) * (5.0/9)
