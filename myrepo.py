import sys,re,os
from subprocess import *
from xml.sax import make_parser, handler

class MyHandler(handler.ContentHandler):
  def startElement(self, name, attrs):
    print 'Start Tag:', name
    if name == 'project':
      project_name = attrs.getValue('name')
      print '--name:' + project_name
      project_path = attrs.getValue('path')
      print '--path:' + project_path
      m = re.match('(accepted|submit)\/(tizen|tizen_2.1_compat|tizen-ivi-release)\/\d+\.\d+-0-g(\w+)',attrs.getValue('revision'))
      project_revision = m.group(3)
      print '--version:' + project_revision
      call(['git','clone','tizen:' + project_name, project_path])
      #p.wait()
      pid = os.fork()
      if pid:
        pid, status = os.wait()
      else:
        print ':test:'+ os.getcwd()
        os.chdir(os.path.join(os.getcwd(),project_path))
        print ':test:'+ os.getcwd()
        os.execv('/usr/bin/git', ('git','reset','--hard', project_revision))
      #p.wait()

parser = make_parser()

h = MyHandler()
parser.setContentHandler(h)

parser.parse(sys.argv[1])
print sys.argv[1]



