import sys
import os 

def travel_gyp(repath):
  print 'travel ' + repath
  dirs = []
  for f in os.listdir(repath):
    #print f
    if os.path.islink(f):
      continue
    if os.path.isdir(f):
      if f != '.git' and f != '.svn':
        dirs.append(f)
    elif os.path.isfile(f):
      print f

  for d in dirs:
    travel_gyp(os.path.join(repath + d))

def find():
  travel_gyp(os.getcwd())
 
