from turtle import *

def get_dimention(input_string, error_string):
    res = input(input_string)
    if not res.isdigit() or float(res) <= 0:
        print (error_string)
        return get_dimention(input_string, error_string)
    return float(res)

def get_coordinate(input_string, error_string):
    res = input(input_string)
    if not res.lstrip('-').isdigit():
        print (error_string)
        return get_dimention(input_string, error_string)
    return float(res)

def move(z, t, xd = 10, yd = 10):
    position = {
    'x': z * xd,
    'y': t * yd
    }
    goto(position['x'], position['y'])