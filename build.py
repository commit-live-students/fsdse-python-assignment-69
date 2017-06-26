import numpy as np
def solution(array):
    input_arr = np.array(array)
    centi = (input_arr-32)*5/9
    return centi
