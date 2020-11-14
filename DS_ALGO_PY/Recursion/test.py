# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:32:39 2020

@author: Jagadeesh
"""

import os

print (os.listdir("."))
n=(os.listdir("."))
for i in n:
    
    print (os.path.isfile(str(i)))