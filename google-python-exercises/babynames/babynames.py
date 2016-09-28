#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def read_html(filename):
  f = open(filename,'r')
  raw_text = f.read()
  f.close()
  return raw_text

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  raw_text = read_html(filename)  
  
  #searching for the year
  year = re.search('(<h3 align="center">Popularity in )(\d\d\d\d)',raw_text).group(2)
  
  #searching for the list of names
  list_of_names = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',raw_text)
  
  #pair each name with it's rank
  name_and_rank = []  
  for line in list_of_names:
    name_and_rank.append((line[1], line[0]))
    name_and_rank.append((line[2], line[0]))
  
  # sort the list alphabetically
  name_and_rank = sorted(name_and_rank, key = lambda x:x[0])
  name_and_rank = dict(name_and_rank)

  return year, name_and_rank

### testing
#a=extract_names('baby1990.html')
#b=a[1]
#dicti = {'a':1,'b':2}
#for k,v in dicti.items():
#    print k,v


def write_summary(filename):
  extracted_object = extract_names(filename)
  year = extracted_object[0]
  ranked_names = extracted_object[1]
  
  new_name = '{}-summary.txt'.format(year)
  f = open(new_name,'w')
  for k,v in ranked_names.items():
    line = '{} {}\n'.format(k,v)    
    f.write(line)
  f.close()
      
  return '{}-summary.txt successfully written'.format(new_name)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  if len(sys.argv) != 3:
    print 'usage: babynames.py {--summary | --print} filename'
    sys.exit(1)  
  
  option = sys.argv[1]
  filename = sys.argv[2]
  
  if option == '--summary':
    print write_summary(filename)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  if option == '--print':
    print extract_names(filename)
  
if __name__ == '__main__':
  main()
