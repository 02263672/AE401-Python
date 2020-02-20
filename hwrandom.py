# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:38:59 2020

@author: Dora
"""
name = ['Erina','Queenie','Hank','Sana','Yuna',]
verb = ['玩','看','寫','摺','吃']
noun = ['Jacket','Computer','Tape','Horse','Sibling']
import random
def random_list(list1):
    word = random.sample(list1,1)[0]
    return word

def random_sentence(name,verb,noun):
    sentence = random_list(name) + random_list(verb) + random_list(noun)
    return sentence
    
for _  in range(10):
    print(random_sentence(name,verb,noun))