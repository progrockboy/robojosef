# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:52:18 2021

@author: nickg
"""

import random

questions = []

roboStalin = True

welcome = ['ROBO STALIN IS ACTIVATE', 
           'YOU MAY SUBMIT YOUR QUESTIONS', 
           'BY TYPING "whatSaysJosef()"']

messages =  ['YOUR CONTRIBUTION WILL BE REWARDED COMRADE',
    'LET THE VODKA BE YOUR ANSWER',
    'DA! IT IS THE CASE!',
    'I HAVE MUCH TO TO THINK ABOUT AT THE MOMENT',
    'DO NOT BOTHER THE PREMIER AT THIS TIME',
    'YOUR NEEDS ARE NOT CLEARLY IN FOCUS',
    'NYET',
    'IT LOOKS BAD',
    'BLYAT',
    'DOUBTLESS THIS IS YOUR FAULT',
    'YOU SHALL BE REMOVED FROM HISTORY FOR YOUR FAILURES',
    'I WOULD NOT EXPECT THIS THING TO HAPPEN']

def whatSaysJosef():
    print(messages[random.randint(0, len(messages) - 1)])


def main():
    for w in welcome:
        print(w)
    while roboStalin:
        q = input('Have you got a question?')
        if q == "" or q == "no":
            
            break
        questions.append(q)
        whatSaysJosef()        
    
        
    
    
if __name__ == '__main__':
    main()
    
    if roboStalin == False:
        roboStalin = True
        
            

