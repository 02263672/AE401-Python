# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:01:24 2020

@author: Dora
"""
import os.path
d = {}


print('##############')
print('####歡迎進入將英文系統####')
print('##############')
print('**使用本系統，成為英文高手**')

if os.path.isfile('engdictionary.txt'):
    fo = open('engdictionary.txt','r')
else:
    fo = open('engdictionary.txt','w')
for i in fo.readlines():
    data = i.split(':')
    
    key = data[0]
    value = data[1]
    
    value = value.strip()
    
    d[key] = value
fo.close()
    
while True:
    print('=>')
    print('1. 建立詞彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')
    
    sol = input('輸入要執行的選項:')
    if sol == '1':
        while True:
            voc = input('輸入新單字(按0跳出):')
            if voc =='0':
                break
            if voc not in d:
                m = input('輸入中文解釋:')
                d[voc] = m
            else:
                print("字典已經有此單字了")
        print(d)
        if os.path.isfile('engdictoinary.txt'):
            fo = open('engdictionary.txt','a')
        else:
            fo = open('engdictionary.txt','w')
        for k,v in d.items():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('\n')
        
        fo.close()    
    if sol == '2':
        if not os.path.isfile('engdictionary.txt'):
            print('目前字典不存在')
            
        else:
            fo = open('engdictionary.txt','a')
            print(fo.read())
            fo.close()
        
    if sol == '3':
        eng = input('輸入要翻譯的英文單字(按0跳出):')
        if eng =='0':
            break
        if eng in d:
            print(d[eng])
        else:
            print("This dictionary didn't include this word")
    if sol == '4':
        chi = input('輸入要翻譯的中文單字(按0跳出):')
        if chi =='0':
            break
        for k,v in d.items():
            if chi == v:
                print(v,"'s translation is",k)
                break
        else:
            print('Sorry, there is no this word in the dictionary')
                
    if sol == '5':
        score = 0
        print('The total score is', len(d), 'points')
        for k,v in d.items():
            ans = input(v +':')
            if ans == k:
                score += 1
                print('Correct, you got',score,'points now')
            else:
                print('Wrong, you got',score,'points now')
    if sol == '6':
        break
    else:
        print("只能輸入1~6而已")