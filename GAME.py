# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:07:45 2019

@author: Pranjal
"""
import random

def choose():
    words=['elephant','education','agra','pranjal','egypt']
    pick=random.choice(words)
    return pick

def jumble(words):
    jumbled="".join(random.sample(words,len(words)))
    return jumbled

def thank(p1name,p2name,pp1):
    print(p1name,"thank you")
    print(p2name,"thank you")
    print("have a nice day")

def play():
    p1name=input("enter the name of p1")
    p2name=input("enter the name of p2")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if(turn%2==0):
            print(p1name,"p1 your turn\n")
            ans=input("enter ans")
            if ans==picked_word:
                pp1=pp1+1
                print("your score is ",pp1)
            else:
                print("better luck")
            c=int(input("want to contiue")) 
            if c==0:
                thank(p1name,p2name,pp1)
                break
            
        else:
            print("p2 your turn")
            ans=input("enter ans:")
            if ans==picked_word:
                pp2=pp2+1
                print("your score is ",pp2)
            else:
                print("better luck")
            c=int(input("want to contiue"))
            if c==0:
                thank(p1name,p2name,pp1)
                break
        turn=turn+1
    if(pp1>pp2):
        print("you are legend",p1name)
    else:
        print("you are legend",p2name)
play()



            
            