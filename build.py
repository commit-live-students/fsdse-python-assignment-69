import numpy as np



def solution(array):
    input = np.array(array)
    output = ((input - 32) * 5/9)
    return output
