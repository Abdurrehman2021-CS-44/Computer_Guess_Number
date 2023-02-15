# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:41:54 2022

@author: USER
"""

import random

def guess_computer(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low < high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} number, too high(H), too low(L), or correct(C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print ("Yay, The computer guessed your number correctly!")
    
def main():
    guess_computer(1000)

if __name__ == "__main__":
    main()