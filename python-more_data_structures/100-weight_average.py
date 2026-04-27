#!/usr/bin/python3
def weight_average(my_list=[]):
    return 0 if not my_list else sum(a*b for a, b in my_list) / sum(b for a, b in my_list)
