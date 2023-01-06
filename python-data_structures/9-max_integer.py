#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == " ":
        return "None"
    big_value=0
    for i in my_list:
        if i > big_value:
            big_value=i
    return (big_value)
