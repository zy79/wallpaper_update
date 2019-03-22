# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:11:46 2019

To scan and backup latest windows wallpaper update.

@author: Yu
"""

import glob
import os
from os.path import expanduser
from shutil import copyfile
from os import listdir
from os.path import isfile, join

home = expanduser("~")
# your own path to save pics
targetpath = home + '/Desktop/pics/'
# path where windows put pics
sourcepath = home + '/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'

# get latest modified date in target parth
targetfiles = glob.glob(targetpath+'*')
latestfile = max(targetfiles, key=os.path.getmtime)
# get time threshold
timethreshold = os.path.getmtime(latestfile)
# read in all file names excluding folders
sourcefiles = [f for f in listdir(sourcepath) if isfile(join(sourcepath, f))]
# get latest modified date in source, only for files > 200k
file_list = [x for x in sourcefiles if os.path.getsize(sourcepath+x)>200000 and os.path.getmtime(sourcepath+x)>timethreshold]

#copy files
if file_list != []:
    for file in file_list:
        copyfile(sourcepath+file, targetpath+file+'.jpg')
