import sys
import xbmc
import xbmcaddon

import os
import os.path

ID    = 'script.module.extrocore'
ADDON = xbmcaddon.Addon(ID)
PATH  = ADDON.getAddonInfo("path")
LIB   = xbmc.translatePath( os.path.join(PATH, 'lib' ) ).decode("utf-8")

sys.path.append(LIB)

import ExtroCore

if len(sys.argv) > 1 :
  if sys.argv[1] == 'rebootAndroid':
      rebootAndroid()
  elif sys.argv[1] == 'rebootLinux':
      rebootLinux()
  elif sys.argv[1] == 'rebootDebian':
      rebootDebian()
