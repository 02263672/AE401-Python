# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:42:38 2020

@author: Dora
"""

x=input("數學成績:")
y=input("英文成績:")
x=int(x)
y=int(y)
z=int(x+y)
if x< 60 and y< 60:
    print("不太理想!")
elif x >= 90 and y >= 90:
    print("獎勵!")
else:
    print("再加油")
    
    