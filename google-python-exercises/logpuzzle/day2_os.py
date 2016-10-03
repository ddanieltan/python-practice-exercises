# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:09:47 2016

@author: ddan
"""
import sys
import os
import commands

#dir(os)

def list_directory(dir1):
  cmd = 'ls -l ' + dir1
  (status,output) = commands.getstatusoutput(cmd)
  if status: #if status is non-zero
    sys.stderr.write('there was an error' + output)
    sys.exit(1) #exit the script
  print output

#  filenames = os.listdir(dir1)
#  for filename in filenames:
#    path = os.path.join(dir1,filename)
#    print path
#    print os.path.abspath(path)
  
  
def main():
  list_directory(sys.argv[1])

if __name__ == '__main__':
  main()

# os.path.exists()

# import shutil
# shutil.copy(source,dest)

# import commands
# commands.getstatusoutput(cmd)
