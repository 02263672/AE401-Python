# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:11:39 2020

@author: Dora
"""
"""
d = {'Alice':1009,'Bill':2019}
len(d)

dic = {'apple':'蘋果','orange':'橘子'}
a = input('輸入英文單字:')
b = input('輸入中文單字:')

dic [a] = b
print(dic)



"""
d = {}

print('##############')
print('####歡迎進入將英文系統####')
print('##############')
print('**使用本系統，成為英文高手**')
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
    if sol == '2':
        a = sorted(d)
        for i in a:
            print(i, 'is', d[i])
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

