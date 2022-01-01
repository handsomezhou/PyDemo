# -*- coding: utf-8 -*-
# @Time : 2021/9/22
# @Author : handsomezhou
import random

from constant import Constant


def is_zero(value: float):
    isZero = False

    value_4_float =float(value)
    if value_4_float> -Constant.ZERO_OF_FLOAT_BOUNDARY and value_4_float < Constant.ZERO_OF_FLOAT_BOUNDARY:
        isZero = True

    return isZero

def is_empty(value:str):
    empty=True
    if value is None:
        return empty

    if len(value)<=0:
        return empty

    empty=False

    return empty

def get_bool_value(value:str):
    bool_value=None
    if value is None:
        return bool_value

    if value == str(True):
        bool_value=True
        return bool_value

    if value == str(False):
        bool_value=False
        return bool_value

    return bool_value

def get_asterisk(value:str):
    asterisk=Constant.NULL_STRING
    if value is None:
        return asterisk

    password_len=len(value)
    for i in range(password_len):
        asterisk +=Constant.ASTERISK

    return asterisk

def random_int( min:int, max:int):
    min_value = min
    max_value = max

    if min > max:
        min_value=max
        max_value=min

    return random.randint(min_value,max_value)

if __name__ == '__main__':
    value=float(0.00000001)
    print(is_zero(value))
    print(is_zero(0.000000001))
