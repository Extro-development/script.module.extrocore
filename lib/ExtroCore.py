##
#
# Copyright (C) 2016 - Stanislav Vlasic <svlasic@gmail.com>
# This program is Free Software see LICENSE file for details
#
##

import sys
import xbmc
import xbmcaddon

import os
import os.path

ID    = 'script.module.extrocore'
ADDON = xbmcaddon.Addon(ID)
PATH  = ADDON.getAddonInfo("path")

def log(text):
    xbmc.log("[ExtroCore] : %s" % str(text))

def getProdname():
    f = open('/etc/prodinfo/prodname').read()
    return f.rstrip("\n").rstrip("\r")

def deviceSuspend():
    log('Suspend device')
    xbmc.executebuiltin('Suspend')

def rebootAndroid():
    log('Reboot to Android started')
    retvalue = -1
    retvalue = os.system('fw_setenv forcedroid 1')
    log("Setting variable returned: %s" % str(retvalue))
    xbmc.executebuiltin('XBMC.Reset()')

def rebootLinux():
    log('Reboot to Linux started')
    retvalue = os.system('fw_setenv forcelinux 1')
    log("Setting variable returned: %s" % str(retvalue))
    xbmc.executebuiltin('XBMC.Reset()')

def debianInstalled():
    if os.path.exists("/storage/.debian/etc/%s/versions" % _getProdname()):
        return True
    else:
        return False

def rebootDebian():
    if debianInstalled():
        log('Reboot to Debian started')
        retvalue = os.system('fw_setenv forcedebian 1')
        log("Setting variable returned: %s" % str(retvalue))
        xbmc.executebuiltin('XBMC.Reset()')
    else:
        log("Debian is not installed")
