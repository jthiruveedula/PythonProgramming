# Examining Runtime

- Runtime is important factor when thinking about efficiency 

- This allow us to pick optimal coding approach(Faster code == more efficient code)

- Calculating runtime using IPython commands(%timeit) which only available in jupyter and IPython

```
%timeit nums = np.random.rand(1000)
output: 19 µs ± 1.19 µs per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```
**Using timeit we can analyse for specific runs/loops as well**

In below eg r-->runs and n-->num of loops
```
%timeit -r2 -n10 nums = np.random.rand(1000)
output: 65.5 µs ± 37.9 µs per loop (mean ± std. dev. of 2 runs, 10 loops each)
```

Based on this we can analyse best and worst part of our code and rectify it.

Example:- Below analysis show time consumption for creating dictionary using formal method and literal method

```
#formal method
%timeit dic = dict()
output: 281 ns ± 31.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
#literal method
%timeit dic1 = {}
output: 74.7 ns ± 8.22 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```
We can see literal method is pretty faster in creating dictionary.

# Code Profiling 

- Detailed stats on frequency and duration of function calls
- line by line analysis

Before diving into this, we need to install __line_profiler__ package

``pip3 install line-profiler``

Using load_ext we can load line profiler

``%load_ext line_profiler``

Define any function for testing and use **lprun -f** for analyzing function, We can see ouput of this funcion in tabular format.

```
def square(n):
    return n*n
%lprun -f square square(100)
output:

Timer unit: 1e-07 s

Total time: 2.81e-05 s
File: <ipython-input-12-2e290af5017e>
Function: square at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def square(n):
     2         1        281.0    281.0    100.0      return n*n
```

In above output we need to focus on PerHit time and %Time based on thie we can modify our code.

# Code profiling for Memory analysis

- Detailed stats on memory consumption
- line-by-line analysis

**Installing memory-profiler is same as line-profiles**

``pip3 install memory-profiler``

- Function must be imported when using memory-profiler

```
from square import square
%load_ext memory_profiler
%mprun -f square square(100)
output:

Filename: C:\Users\Jagadeesh\Desktop\python\practice\square.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     1     47.5 MiB     47.5 MiB           1   def square(n):
     2     47.5 MiB      0.0 MiB           1       if n>=1:
     3     47.5 MiB      0.0 MiB           1           return n*n
     4                                             else:
     5                                                 n
```

- Here we need to focus on Mem usage and Increment (Will show per line)


