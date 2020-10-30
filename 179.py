#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:51:54 2019

@author: rasmuser
"""

import math
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))

num = 1
l1 = len(divisors(num))
lim = 10**7+1
count = 0

for k in range(2,lim):
    l2 = len(divisors(k))
    if l1==l2:
        count = count + 1
    l1 = l2