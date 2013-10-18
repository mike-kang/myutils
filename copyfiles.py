#!/usr/bin/python

import os
import sys
import shutil

def copyfiles():
  f = open(sys.argv[3])
  for line in f:
    src = os.path.join(sys.argv[1],line.strip())
    dst = os.path.join(sys.argv[2],line.strip())
    print 'copy ' + src + ' ' + dst
    shutil.copyfile(src, dst)
  

if __name__ == '__main__':
  if len(sys.argv) < 4:
    print '[Usage] %s original modified filename'% sys.argv[0]
    sys.exit()
  m = copyfiles()
