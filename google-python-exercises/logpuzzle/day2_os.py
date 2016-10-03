# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:09:47 2016

@author: ddan
"""
import sys
import os

#dir(os)

def list_directory(dir1):
  filenames = os.listdir(dir1)
  return filenames
  
def main():
  print list_directory(sys.argv[1])

if __name__ == '__main__':
  main()
  