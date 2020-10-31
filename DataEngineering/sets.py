#Branch of Mathematics applied to collection of objects
#i.e., sets

#Python has built in set datatype with accompanying methods
# instersection (all elements that are in both sides)
#difference(elements in one set but not in other set)
#symmetric_difference(all elements in exactly one set)
#union ( all elements that are in either set)

lstA= ['Horse','Lion','cheeta','deer','parrot']
lstB = ['Peacock','humming','pigeon','parrot']

setlsta=set(lstA)
setlstb=set(lstB)
intersect=setlsta.intersection(setlstb)
print("Intersection for both sets at:",intersect)
diff = setlsta.difference(setlstb)
print("Difference between seta and setb is: ",diff)
symdiff = setlsta.symmetric_difference(setlstb)
print("Symmetric Difference: ",symdiff)
unionout = setlsta.union(setlstb)
print("Union of both sets: ",unionout)

# output:
# Intersection for both sets at: {'parrot'}
# Difference between seta and setb is:  {'Horse', 'cheeta', 'deer', 'Lion'}
# Symmetric Difference:  {'humming', 'Horse', 'cheeta', 'pigeon', 'deer', 'Lion', 'Peacock'}
# Union of both sets:  {'humming', 'Horse', 'cheeta', 'Peacock', 'pigeon', 'deer', 'parrot', 'Lion'}