# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:20:10 2020

@author: Dora
45
"""

w= input("weight:")
h= input("height(meter):")
bmi = int(w)/float(h)** 2
print("bmi :", bmi)
if bmi<18.5:
    print("過輕")
elif bmi >= 18.5 and bmi <= 24:
    print("正常")        
else: 
    print("過重")
    