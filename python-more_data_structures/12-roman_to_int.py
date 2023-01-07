#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str or None:
        return 0
    d={'I':1, 'V':15, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and d[roman_string[i]] < d[roman_string[i]]:
            ans = ans - d[roman_string[i]]
        else:
            ans = ans + d[roman_string[i]]
        return ans
