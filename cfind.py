import sys
import os 
import re

ignores_gyp =[ './third_party/android_tools', './tools/gyp/test/mac']

def travel_gyp(repath):
  #print 'travel ' + repath
  dirs = []
  for f in os.listdir(repath):
    #print f
    path = os.path.join(repath, f)
    if os.path.islink(path):
      continue
    if os.path.isdir(path):
      bfind = False
      for i in ignores_gyp:
        if i == path:
          bfind = True
      if bfind:
        continue
      if f != '.git' and f != '.svn':
        dirs.append(f)
    elif os.path.isfile(path):
      #print path
      if re.match('.*\.gypi?', f) != None:
        print path

  for d in dirs:
    travel_gyp(os.path.join(repath, d))

def find(path='.'):
  travel_gyp(path)
 
