# Numpy
## Power of Numpy array's

**Numpy arrays provides fast and memory efficient approach to python list**

**Numpy arrays are homogeneous**

In below example due to homogeneous nature it is converting integers into float.
```
import numpy as np
x=np.array([2,3,-0.3,5,1])
print(x)
output: [ 2.   3.  -0.3  5.   1. ]
-- Checking data type of numpy array
print(x.dtype)
output: float64
```  
**Numpy array has BroadCasting functionality** 

```
nums = np.array([2,4,1,6,8,3])
print(nums ** 2)
output: [ 4 16  1 36 64  9]
```
**Numpy is efficient in indexing capability** 
```
import numpy as np

nums = [[12,32,43],
        [15,72,87]]
nparray = np.array(nums)
print("for fetching 2 element in 1st row: ", nparray[0,1])
print("for fetching 1st columns: ",nparray[:,0])
print("for fetching 2nd row: ",nparray[1:])  
output:
for fetching 2 element in 1st row:  32
for fetching 1st columns:  [12 15]
for fetching 2nd row:  [[15 72 87]]
```
**Boolean Indexing**
```
nums = [[12,32,43],
        [15,72,87]]
nparray = np.array(nums)
print(nparray>0)
output: 
[[ True  True  True]
 [ True  True  True]]
```
