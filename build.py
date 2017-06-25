import numpy as np

def solution(array):
    Centigrade = []
    for i in array:
        f_c = (i - 32) * (5.0 / 9.0)
        Centigrade = np.append(Centigrade, f_c)
    return Centigrade
