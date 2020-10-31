# this module is fast for generating combinations despite of creating nested for loops
from itertools import combinations

lst = ['apple','ball','cat','dog','elephant']

#combinations(lst,3) function used to generate combination of 3 elements in a group

comb = combinations(lst,3)
print(comb)
unpack = [*comb]
print("Unpacked output:",unpack)

#Unpacked output: [('apple', 'ball', 'cat'), ('apple', 'ball', 'dog'), ('apple', 'ball', 'elephant'), ('apple', 'cat', 'dog'), ('apple', 'cat', 'elephant'), ('apple', 'dog', 'elephant'), ('ball', 'cat', 'dog'), ('ball', 'cat', 'elephant'), ('ball', 'dog', 'elephant'), ('cat', 'dog', 'elephant')]
