# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:38:04 2020

@author: Jagadeesh
"""


def arrayReversal(arr,start,end):
    while start < end:
#shuffling start and end point of array 
        arr[start],arr[end]=arr[end],arr[start]
        start += 1
        end -= 1
    return " ".join(map(str,arr)) 

    
arr=[1,2,3,4,5,3]

end = len(arr)-1

print(arr)

print("Reversed Array is :-")
print(arrayReversal(arr, 0, end))
    


