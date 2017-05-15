#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:56:16 2017

@author: tylerlawson
"""
####################################
# Computer Project #2
#
#   Algorithm
#        Prompt the user for a number of squares in range [1-10]
#        draw and fill the squares by using turtle graphics with random colors
#        end program
#
#####################################




import turtle #import tools necessary
import random
import time



def pick_color(): #prick a random color to draw and fill with
    colors=["blue","red","yellow","green","orange","turquoise","pink"]
    random.shuffle(colors)
    
    return colors[0]

numSquares = int(input("how many squares?(1-10) "))
    #prompt and save user for number of squares

if (numSquares<=0):
    #make sure the inputted number will work 
    #and if it is outside the range stop the program
    print("I told you to pick between 1 and 10, goodbye")
    turtle.bye()#end program
    
   
x = -200
y = 200#assign variables the coordinates that will be used
z=400#assign variable for length of lines drawn

for i in range(numSquares):#draw number of squares assigned by user
    turtle.color(pick_color())#assign the random color to the turtle
    turtle.up()#pick up the turtle
    turtle.goto(x,y)#move the turtle
    turtle.down()#put down the turtle
   
    turtle.begin_fill()#fill the square
    
    for i in range(4):#move for each side of the square
        turtle.forward(z)
        turtle.right(90)
        
    turtle.end_fill()
    x +=20#reassign coordinates and length of lines
    y -=20
    z-=40
    
time.sleep(10)#pause for 10 seconds
turtle.bye()#close program