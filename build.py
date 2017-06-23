import numpy as np



def solution(array):
    list_f = array
    list_c = []
    for f in list_f:
        c = (f - 32)*5./9
        list_c.append(c)
    return list_c
