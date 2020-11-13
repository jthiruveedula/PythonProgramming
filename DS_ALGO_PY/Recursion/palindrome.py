# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 01:08:21 2020

@author: Jagadeesh

Palindrome 
A word that is the reverse of itself and it is the same word when read forwards and backwards.
eg: ara --> ara
madam --> madam
"""

def palindrome_check(input):
    """ 
    Parameters
    ----------
    input : string
    -------
    output : True if input is palindrome else false
    """
 
    if len(input) <= 1:
        return True
    elif len(input) == 2:
        return input[0] == input[1]
    else:
        output = (input[0] == input[len(input)-1]) & (palindrome_check(input[1:len(input)-1]))
        return output
    
print(palindrome_check('madam'))


#test cases
print ("Pass" if  (palindrome_check("madam")) else "Fail")
print ("Pass" if  (palindrome_check("abba")) else "Fail")