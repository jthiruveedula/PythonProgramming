# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:31:35 2020

@author: Jagadeesh

Find pair with given sum

"""
# =============================================================================
#time complexity o(n*2) time 0(1) space
# def sumPair(arr,sumVal):
#     
#     for i in range(len(arr) -1):
#         
#         for j in range(i+1,len(arr)):
#             
#             if arr[i] + arr[j] == sumVal:
#                          
#                 print("Sum pair found by adding {} + {} = {}".format(arr[i],arr[j],sumVal))
#             
#     else:
#         print("Sum paring couldn't be done using values in array!")
# =============================================================================

#=============================================================================
#  o(n) | O(n) space
def sumPair(arr,sumVal):
    nums={}
    for num in arr:
        potientialMatch=sumVal -num
        if potientialMatch in nums:
            return [potientialMatch,num]
        else:
            nums[num] = True

#=============================================================================


# =============================================================================
# O(n log n) | O(1) space
# def sumPair(arr,sumVal):
#     arr.sort()
#     left = 0
#     right =len(arr)-1
#     while left < right:
#         currentSum = arr[left] + arr[right]
#         if currentSum == sumVal:
#             return [arr[left],arr[right]]
#         elif currentSum < sumVal:
#             left += 1
#         elif currentSum > sumVal:
#             right -= 1
#             
#     return []
# =============================================================================
    

   
mylist=[1,5,6,7,9,2,8,9]
arr=list(dict.fromkeys(mylist))
print(arr)
sumVal=17
print(sumPair(arr, sumVal))
