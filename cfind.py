import sys
import os 
import re

class cfind(object):
  def __init__(self, ignore, regex):
    self.ignore = ignore
    self.regex = regex
  
  def travel(self, repath):
    #print 'travel ' + repath
    if self.ignore in os.listdir(repath):
      return

    dirs = []
    for f in os.listdir(repath):
      #print f
      cpath = os.path.join(repath, f)
      if os.path.islink(cpath):
        continue
      if os.path.isdir(cpath):
        if f != '.git' and f != '.svn':
          dirs.append(f)
      elif os.path.isfile(cpath):
        #print path
        if re.match(self.regex, f) != None:
          print cpath

    for d in dirs:
      self.travel(os.path.join(repath, d))

def find_gyp(path='.'):
  f = cfind('.nogyp', '.*\.gypi?')
  f.travel(path)
 
def find_c(path='.'):
  f = cfind('.noc', '.*\.(c|cc|cpp)')
  f.travel(path)

def find_h(path='.'):
  f = cfind('.noh', '.*\.h')
  f.travel(path)

def find_java(path='.'):
  f = cfind('.nojava', '.*\.java')
  f.travel(path)

