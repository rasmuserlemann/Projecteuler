#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:51:54 2019

@author: rasmuser
"""

L = []
for k in range(7,100):
    for kk in range(2,100):
        N = k**kk
        digits = list(str(N))
        S = 0
        for elem in digits:
            S = S + int(elem)
        if S==k:
            L.append(N)
            
print(sorted(L)[30])