## DataEngineering made easy with Python
## Python Buit-in Functions
Built-in functions give easy and efficient way to operate.

- print()
- len()
- range()
- round()
- enumerate()
- map()
- zip() 

__Coding part__ for these built in functions

#print()
```
print("Hello print")
Hello print
```
#len()
 ```
print(len("hello"))
5
```
#range()
Suppose if we want to create a list of 10 integers, for that we need to explicitly type out each integer.

If we use range function that will create for us by specifying start, stop value and step in case needed.
#range(start,stop,step) function with out step
```
nums=range(1,11)
nums_list = list(nums)
print(nums_list)
output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
#range(start,stop,step) function with step
 ```
nums=range(1,11,2)
nums_list = list(nums)
print(nums_list)
output: [1, 3, 5, 7, 9]
```
We can directly specify stop point, It would pick start range from 0.
```
nums=range(11)
nums_list = list(nums)
print(nums_list)
output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
#round()
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

The default number of decimals is 0, meaning that the function will return the nearest integer.
```
x = round(5.76543)
print(x)
output: 6
- Round a number to only two decimals:
x = round(5.76543,2)
print(x)
output: 5.77
```
#enumerate()
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

```
l1 = ["eat","sleep","repeat"] 
s1 = "Code"
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("List Enum: ",list(obj1))
print("String Enum: ",list(obj2))
output:
List Enum:  [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
String Enum:  [(0, 'C'), (1, 'o'), (2, 'd'), (3, 'e')]

-- We can change start index for index position

obj1 = enumerate(l1,2)
obj2 = enumerate(s1)
print("List Enum start index=2: ",list(obj1))
print("String Enum: ",list(obj2))
List Enum start index=2:  [(2, 'eat'), (3, 'sleep'), (4, 'repeat')]
String Enum:  [(0, 'C'), (1, 'o'), (2, 'd'), (3, 'e')]
```
#map(fun, iter)
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
```
numbers=[2.3,5.2,4.1,5.67,7.02]
out=map(round,numbers)
print(list(out))
output: [2, 5, 4, 6, 7]
```
#map() with lambda function
```
numbers=[1,2,3,4,5]
sqrt= map(lambda x: x*x, numbers)
print(list(sqrt)) 
output: [1, 4, 9, 16, 25]
```
#zip()
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

```
a = ("John", "Charles", "Mike")
b = ("Jenny-b", "Christy-b", "Monica-b", "Vicky-b")
c = ("Jenny-c", "Christy-c", "Monica-c", "Vicky-c")
x = zip(a, b,c)
print(list(x))
output: [('John', 'Jenny-b', 'Jenny-c'), ('Charles', 'Christy-b', 'Christy-c'), ('Mike', 'Monica-b', 'Monica-c')]
```
 