# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:35:53 2020

@author: Dora
"""

dic = {}

while True:
    print('1: add new word','2: Searching(Eng to Chi)','3: Searching(Chi to Eng)','4:Show the dictionary')
    num = int(input('輸入欲執行之代碼'))
    
    if num==1:
        numvoc = int(input('how many words do you want to add to dictionary?'))
        for i in range(numvoc):
            vocabulary = str(input('Type English vocab:'))
            definition = str(input('Type Chinese definition:'))
            dic[vocabulary] = definition
    elif num ==2:
        engvoc = str(input('輸入欲查詢之英文單字:'))
        if engvoc not in dic:
            print("didn't have the definition yet")
        else:
            print('解釋為:',dic[engvoc])
            
    elif num == 3:
        chivoc = str(input('輸入欲查詢之中文單字'))
        
        temp = 0
       
        for k,v in dic.items():
            if chivoc == v:
            print(k)
            temp = 1
            
    elif num ==4:
        print(dic)
            
    
    