#sometimes we can't eliminate the necessity of of loops in that case how could we write better loops

# writing better loops

# understanding what is being done with each loop iteration
# move one-time calculations outside(above) the loop
# use holistic conversions outside(below) the loop
# anything that is done once should be outside the loop

import numpy as np

empName =['Jagadeesh','Richard','Darren','Paul']
empSalary = np.array([30000,40000,25000,15000])

#Calculating average salary outside loop
avgSalary = empSalary.mean()

for name,sal in zip(empName,empSalary):
    if sal>avgSalary:
        print("{}'s salary is greater than average salary : {} and his salary is {}".format(name,avgSalary,sal))
