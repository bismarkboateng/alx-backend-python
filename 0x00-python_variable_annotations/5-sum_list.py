#!/usr/bin/env python3\
from typing import List


'''
a type-annotated function sum_list
which takes a list input_list of floats
as argument and returns their sum as a float.
'''


def sum_list(input_list: List[float]) -> float:
    '''
    params: input_list
    return: float
    '''

    return sum(input_list)
