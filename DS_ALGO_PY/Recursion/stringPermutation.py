# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 01:28:14 2020

@author: Jagadeesh

string permutations
"""


def permutations(l):
    """
    :param: input string('abs')
    Return - list of all permutations of the input string
    ['abs', 'bas', 'bsa', 'asb', 'sab', 'sba']
    """
    if len(l) <= 1:
        return [l]

    elif len(l) == 2:
        return [l, l[::-1]]

    else:
        output = []
        current_level = l[0]
        prev_level = permutations(l[1:])

        for element in prev_level:  # For each answer from previous level
            for pos in range(len(element) + 1):  # For each possible position to put this level value
                temp_list = ''
                temp_element = element
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list += current_level
                    else:
                        temp_list += temp_element[0]
                        temp_element = temp_element[1:]
                        
                output.append(temp_list)
        return output
    
print(permutations('abs'))