# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:36:10 2020

@author: Jagadeesh

String reversal using recursion
"""



def reverse_string(input):
    """
    this function reverse the given input as below
    input --> jagadeesh
    output --> hseedagaj
    """
    if len(input) == 0:
        return ""
    else:
        return reverse_string(input[1:]) + input[0]
    
print(reverse_string('jagadeesh'))


#test cases
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")