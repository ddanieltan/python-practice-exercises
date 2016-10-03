# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:09:56 2016

@author: ddan
"""

import re

#successful match
match = re.search('iig','called piig')
match
match.group()

#unsuccesful match
match_un = re.search('igs', 'called piig')
match_un
match_un.group()

def Find(pattern,text):
  match = re.search(pattern,text)  
  if match:
    print match.group()
  else:
    print 'not found'
    
Find('iig','called piig')

Find('...g','called piig') # . is for any character

Find(r'\.g','called pi.g') # r = raw string, tells python to not do backslash processing

Find(r':\w\w\w','blah blah blah :cat') # \w word character = letters, digits, underscore (usernames)

Find(r':\d\d\d','blah blah blah :cat :123') # \d digit

Find(r'\d\s\d\s\d','blah blah blah 1 2 3 blah blah') #\s whitespace

Find(r'\d\s+\d\s+\d','blah blah blah 1  2          3 blah blah') # + is 1 or more

Find(r':\w+','blah blah blah :kitten blah blah blah') # + is 1 or more, a space is not a word character so it stops

Find(r':\S+', 'blah blah blah :kitten1231233=%&yatta blah blah') # \S is a NON-whitespace character

# [] square brackets can be used to indicate a set of chars, 
# so [abc] matches 'a' or 'b' or 'c'. 
# The codes \w, \s etc. work inside square brackets too 
# with the one exception that dot (.) just means a literal dot.
Find(r'[\w.]+@[\w.]+','blah blah handsome.p@gmail.com blah blah blah @') 

# () parenthesis group the parts you care about
match1 = re.search(r'([\w.]+)@([\w.]+)','blah blah handsome.p@gmail.com blah blah blah @') 
match1
match1.group() #handsome.p@gmail.com
match1.group(1) #handsome.p
match1.group(2) #gmail.com

# findall() doesn't stop at first match, it returns all the matches
match2 = re.findall(r'[\w.]+@[\w.]+','blah blah handsome.p@gmail.com blah ugly@yahoo.com')
match2
#findall has not group() method

# parenthesis will cause findall to return tuples
match3 = re.findall(r'([\w.]+)@([\w.]+)','blah blah handsome.p@gmail.com blah ugly@yahoo.com')
match3

dir(re)
# DOTALL will apply to every line, else . ends at each line
# IGNORECASE 

match1 = re.search(r'([\w.]+)@([\w.]+)','blah blah handsome.p@gmail.com blah blah blah @', re.IGNORECASE) 
