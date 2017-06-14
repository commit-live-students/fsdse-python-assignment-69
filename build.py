import numpy as np


def solution(array):
    newarray = []
    for item in array:
        newarray.append((item-32)*(5.0/9.0))
    return newarray
