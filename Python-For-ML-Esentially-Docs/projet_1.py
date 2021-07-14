# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 01:50:59 2021

@author: Lounes-Kheris
"""

def fibonacci(n):
    a, b = 0,1;
    fib = []
    
    while a < n:
        fib.append(a)
        a, b = b, a+b
        
    return fib