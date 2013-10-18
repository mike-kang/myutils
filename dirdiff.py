#!/usr/bin/python

import os
import sys
import shutil
import filecmp


class dirdiff(object):
  def __init__(self, origin, modified):
    self.origin = origin
    self.modified = modified

    self.f_added_dirs = open("dirdiff_added_dirs", 'w')
    self.f_added_files = open("dirdiff_added_files", 'w')
    self.f_removed_dirs = open("dirdiff_removed_dirs", 'w')
    self.f_removed_files = open("dirdiff_removed_files", 'w')
    self.f_modified_files = open("dirdiff_modified_files", 'w')
  
  def travel(self, repath):
    ''' 
    repath is relative path and directory.
    '''
    print 'travel ' + repath
    origin_dirs=[]
    origin_files=[]
    modified_dirs=[]
    modified_files=[]
    check_dirs=[]
    check_files=[]
    for f in os.listdir(os.path.join(self.origin, repath)):
      t = os.path.join(self.origin, repath, f)
      #print f
      if os.path.islink(t):
        continue
      if os.path.isdir(t):
        if f != '.git' and f != '.svn':
          origin_dirs.append(f)
      elif os.path.isfile(t):
        origin_files.append(f)
    
    for f in os.listdir(os.path.join(self.modified, repath)):
      t = os.path.join(self.modified, repath,f)
      #print f
      if os.path.islink(t):
        continue
      if os.path.isdir(t):
        if f != '.git' and f != '.svn':
          modified_dirs.append(f)
      elif os.path.isfile(t):
        modified_files.append(f)
    
    #print 'origin_dirs: ' + origin_dirs.__str__()
    #print 'modified_dirs: ' + modified_dirs.__str__()
    origin_dirs_clone = [] + origin_dirs
    for f in origin_dirs:
      l = len(modified_dirs)
      try:
        modified_dirs.remove(f)
      except ValueError:
        pass
      if l != len(modified_dirs):
        check_dirs.append(f)
        origin_dirs_clone.remove(f)
    #print 'origin_dirs: ' + origin_dirs_clone.__str__()
    #print 'modified_dirs: ' + modified_dirs.__str__()
    #print 'check_dirs: ' + check_dirs.__str__()
    origin_files_clone = [] + origin_files
    for f in origin_files:
      l = len(modified_files)
      try:
        modified_files.remove(f)
      except ValueError:
        pass
      if l != len(modified_files):
        check_files.append(f)
        origin_files_clone.remove(f)

    for f in modified_dirs:
      self.f_added_dirs.write(os.path.join(repath,f) + '\n') 
    for f in origin_dirs_clone:
      self.f_removed_dirs.write(os.path.join(repath,f) + '\n') 
    for f in modified_files:
      self.f_added_files.write(os.path.join(repath,f) + '\n') 
    for f in origin_files_clone:
      self.f_removed_files.write(os.path.join(repath,f) + '\n') 
    
    for f in check_files:
      try:
        #print f
        if not filecmp.cmp(os.path.join(self.origin,repath,f), os.path.join(self.modified,repath,f)):
          #print 'write: ' + os.path.join(repath,f)
          self.f_modified_files.write(os.path.join(repath,f) + '\n')
      except OSError:
        print 'Error! file compare'
        print os.path.join(self.origin,f)
        print os.path.join(self.modified,f)

   
    #print  check_dirs 
    for f in check_dirs:
      self.travel(os.path.join(repath, f))

  def construct_modified_files_tree(self):
    if os.path.exists('dirdiff_tree'):
        shutil.rmtree('dirdiff_tree')
    os.mkdir('dirdiff_tree')
    origin_root = os.path.join('dirdiff_tree', self.origin.split('/')[-1])
    os.mkdir(origin_root)
   
    f = open('dirdiff_modified_files') 
    for line in f:
        t = os.path.join(origin_root, os.path.dirname(line.strip()))
        if not os.path.exists(t):
            os.makedirs(t) 
    modified_root = os.path.join('dirdiff_tree', self.modified.split('/')[-1])
    shutil.copytree(origin_root, modified_root)
    f.close()
    f = open('dirdiff_modified_files') 
    for line in f:
        os.symlink(os.path.join(self.origin, line.strip()), os.path.join(origin_root, line.strip()))  
        os.symlink(os.path.join(self.modified, line.strip()), os.path.join(modified_root, line.strip()))  
    f.close()
    
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '[Usage] %s original modified'% sys.argv[0]
        sys.exit()
    m = dirdiff(os.path.realpath(sys.argv[1]), os.path.realpath(sys.argv[2]))
    m.travel('')
    
    m.f_added_dirs.close()
    m.f_added_files.close()
    m.f_removed_dirs.close()
    m.f_removed_files.close()
    m.f_modified_files.close()
    
    m.construct_modified_files_tree()
    


    


