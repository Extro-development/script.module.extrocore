import sys
import ExtroCore

if len(sys.argv) > 1 :
  if sys.argv[1] == 'rebootAndroid':
      ExtroCore.rebootAndroid()
  elif sys.argv[1] == 'rebootLinux':
      ExtroCore.rebootLinux()
  elif sys.argv[1] == 'rebootDebian':
      ExtroCore.rebootDebian()
