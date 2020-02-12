# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:39:56 2020

@author: Dora
"""
result = input("成績：")
result=int(result)
if result< 60:
    print("可惜不及格")
elif result> 90:
    print("brilliant!")    
else:
    print("恭喜及格！")
    