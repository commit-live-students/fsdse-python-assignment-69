import numpy as np



def solution(array):
    ls = map(lambda x :((x-32)/1.8),array)
    return ls


solution([0, 12, 45.21, 34, 99.91])
