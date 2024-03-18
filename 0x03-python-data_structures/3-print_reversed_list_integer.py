#!/usr/bin/python3
3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """ will print reversed list in integer"""
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))

