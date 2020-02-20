# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:06:13 2020

@author: Dora
"""

import random
answer = random.randint(1,10)
times=0
while times < 5:
    guess = int(input("what number do you guess?"))
    times= times + 1
    if guess < 1 or guess > 10:
        print("try again")
    else: 
        if answer < guess:
            if times == 5:
                print("guess more than 5 times")
            else:
                print("guess smaller")
        elif answer > guess:
            if times == 5:
                print ("guess more than 5 times")
            else:
                print("guess bigger")
        else :
            print("you win")
            print("you guess ",times,"times")
            break
  
        