import numpy as np



def solution(array):
    """
    Enter your code here
    """
    F = np.array(array)
    celsius = (F - 32) * 5 / 9
    return celsius



solution([0,12,45.21,34.0,99.91])
