import numpy as np



def solution(array):
    """
    Enter your code here
    """
    def to_celsius(far):
        return ((float(far)-32)*5)/9

    v_to_celsius = np.vectorize(to_celsius)

    return v_to_celsius(array)
