import numpy as np



def solution(array):
    array = (np.array(array) - 32)/1.8
    return np.array(array)
