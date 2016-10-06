##
#
# Copyright (C) 2016 - Stanislav Vlasic <svlasic@gmail.com>
# This program is Free Software see LICENSE file for details
#
##

import sys
import subprocess
import xbmc
import xbmcaddon

import os
import os.path

ID    = 'script.module.extrocore'
ADDON = xbmcaddon.Addon(ID)
PATH  = ADDON.getAddonInfo("path")

DEBUG_FLAG = False

def log(text):
    xbmc.log("[ExtroCore] : %s" % str(text))

def fw_setenv(key, value):
    proc = subprocess.Popen(['/usr/bin/fw_setenv', str(key), str(value)], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if DEBUG_FLAG:
        log('fw_setenv: Key: %s; Valie: %s' % (str(key), str(value)))
        log('fw_setenv: output: %s' % str(out))
        log('fw_setenv: error:  %s' % str(err))

def getProdname():
    f = open('/etc/prodinfo/prodname').read()
    return f.rstrip("\n").rstrip("\r")

def deviceSuspend():
    log('Suspend device')
    xbmc.executebuiltin('Suspend')

def rebootAndroid():
    log('Reboot to Android started')
    retvalue = -1
    fw_setenv('forcedroid', '1')
    xbmc.executebuiltin('XBMC.Reset()')

def rebootLinux():
    log('Reboot to Linux started')
    fw_setenv('forcelinux', '1')
    xbmc.executebuiltin('XBMC.Reset()')

def debianInstalled():
    if os.path.exists("/storage/.debian/etc/%s/versions" % _getProdname()):
        return True
    else:
        return False

def rebootDebian():
    if debianInstalled():
        log('Reboot to Debian started')
        fw_setenv('forcedebian', '1')
        xbmc.executebuiltin('XBMC.Reset()')
    else:
        log("Debian is not installed")
