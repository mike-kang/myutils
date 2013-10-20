import sys
import os 
import re

class cfind(object):
  def __init__(self, ignore):
    self.ignore = ignore
  
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
        if self.checkext(f):
          print cpath

    for d in dirs:
      self.travel(os.path.join(repath, d))

class cfind_gyp(cfind):
  def checkext(self, name):
    if name.endswith('.gyp') or name.endswith('.gypi'):
      return True
    return False

class cfind_c(cfind):
  def checkext(self, name):
    if name.endswith('.c') or name.endswith('.cc') or name.endswith('.cpp'):
      return True
    return False

class cfind_h(cfind):
  def checkext(self, name):
    if name.endswith('.h'):
      return True
    return False

class cfind_java(cfind):
  def checkext(self, name):
    if name.endswith('.java'):
      return True
    return False

def find_gyp(path='.'):
  c = cfind_gyp('.nogyp')
  c.travel(path)
 
def find_c(path='.'):
  c = cfind_c('.noc')
  c.travel(path)

def find_h(path='.'):
  c = cfind_h('.noh')
  c.travel(path)

def find_java(path='.'):
  c = cfind_java('.nojava')
  c.travel(path)
