#!/usr/bin/python3
7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """this will adds 2 tuples"""
    ew_tuple = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
