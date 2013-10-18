#!/usr/bin/python
import os
import sys

dest_path = '/data/data/org.chromium.obigo_browser_apk'
result = 'result.txt'

def travel(rpath):
  dirs = []
  for f in os.listdir(rpath):
    print f
    cpath = os.path.join(rpath, f)
    if os.path.isdir(cpath):
      if f != '.svn':
        fd.write('adb shell mkdir ' + os.path.join(dest_path, cpath) + os.linesep)
        print cpath
        dirs.append(f)
    else:
      fd.write('adb push ' + cpath + ' ' + os.path.join(dest_path, cpath) + os.linesep)

  for d in dirs:
    print '2 ' + d
    travel(os.path.join(rpath, d))

fd = open('result.txt','w')
fd.write('adb shell mkdir ' +  os.path.join(dest_path, sys.argv[1]) + os.linesep)
travel(sys.argv[1])
fd.close()

