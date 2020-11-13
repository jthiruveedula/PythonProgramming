# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 01:04:16 2020

@author: Jagadeesh

Factorial using recursion
"""

def factorial(n):
    """
    factorial formula $n! = n * (n-1) * (n-2) ... 1$
    we can use recursive trick to do this
    
    """
    
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
    
    
#test cases
print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")