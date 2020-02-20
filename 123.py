# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:47:14 2020

@author: Dora
"""

import turtle
kennan=turtle.Screen()
kennan.title("I am Dora")
kennan.bgcolor("pink")
hank=turtle.Turtle()
hank.color("white")
hank.shape("turtle")
#ivy=turtle.Turtle()
#ivy.color("blue")
hank.pensize(10)
#ivy.pensize(1)
hank.penup()

times= 0

for i in range(0,20):
    hank.stamp()
    hank.left(45)
    hank.penup()
    hank.forward(times * 3)
    hank.pendown()
    #hank.left(45)
    #hank.forward(30)
    #hank.left(45)
   # hank.forward(40)
    #hank.left(45)
#    hank.forward(50)
    times= times+1
    
hank.done()
kennan.done()
turtle.done()