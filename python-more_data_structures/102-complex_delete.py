#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lst = []
    for i in a_dictionary:
        lst.append(i)
    for k in lst:
        if a_dictionary[k] == value:
            del a_dictionary[k]

