import numpy as np
from scipy.constants import convert_temperature


def solution(array):
    return convert_temperature(np.array(array), 'F', 'C')
