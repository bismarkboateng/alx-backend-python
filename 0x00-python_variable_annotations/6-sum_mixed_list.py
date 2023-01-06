#!/usr/bin/env python3
from typing import Union, List


'''
a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and returns their sum as a float.
'''


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''
    params: mxd_list
    return: float
    '''

    return sum(mxd_list)
