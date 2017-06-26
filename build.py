import numpy as np
def solution(array):
    """
    Enter your code here
    """
    fahrenheit_array = [(((x-32)*5.0)/9.0) for x in array]
    return fahrenheit_array
