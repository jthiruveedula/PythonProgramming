# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 01:37:54 2020

@author: Jagadeesh

mobile keypad combination chars
"""

def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    if num == 0:
        return [""]

    elif num / 10 < 1:
        
        return [element for element in get_characters(num)]

    else:
        input_level = get_characters(num % 10)
        input_prev = keypad(num // 10)
        

        result = []

        for i_a in input_level:
            for i_b in input_prev:
                result.append(i_b + i_a)

        return result
    
print(keypad(97))


