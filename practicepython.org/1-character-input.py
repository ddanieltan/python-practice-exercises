# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:43:53 2016

@author: ddan
"""

#==============================================================================
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 
# Extras:
# 
# Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)
#==============================================================================

import datetime

def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(name + ", you will turn 100 years old in " + 100)

