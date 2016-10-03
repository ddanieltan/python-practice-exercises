# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:09:47 2016

@author: ddan
"""
import sys
import os

#dir(os)

def List(dir):
  filenames = os.listdir(dir)
  print filenames
  
def main():
  List(sys.argv(2))
