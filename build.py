import numpy as np


def solution(array):
    """
    Enter your code here
    """
    F = np.array(array)
    return 5*F/9 - 5*32/9

faces = [0, 12, 45.21, 34, 99.91]
res = solution(faces)
print(res)