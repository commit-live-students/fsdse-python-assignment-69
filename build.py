import numpy as np

def solution(array):
# faren_temp = np.array([ 0., 12., 45.21, 34., 99.91])
    cent_temp = []
    for temp in array:
        temp = (temp - 32)/1.8
        cent_temp.append(temp)
    cent_temp = np.array(cent_temp)
    return cent_temp
