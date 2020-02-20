# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:42:23 2020

@author: Dora
"""
"""
score = [44, 55, 66, 77, 88]

print('highest:',max(score))
print('lowest:',min(score))
print('average:',sum(score)/len(score))

a= sorted(score, reverse =True)
print(a)
print(score)

score.sort(reverse =True)
print(score)
"""
from operator import itemgetter
scores = [
        ['Jennie','G',99],
        ['Rania','J',-1],
        ['Tanya','O',50]]
"""
for i in range(len(scores)):
    for j in range(len(scores[i])):
        print(scores[i][j])
"""     
a = sorted(scores, key = lambda s: s[0])
print(a)

scores.sort(key = lambda s: s[2])
print(scores)

print(sorted(scores, key = itemgetter(1)))