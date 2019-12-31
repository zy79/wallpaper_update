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
from PIL import Image

home = expanduser("~")
home = home.replace('\\', '/')
# your own path to save pics
targetpath = home + '/Desktop/pics/'
tagetvertical = home + '/Desktop/pics/vertical/'
# path where windows save pics
sourcepath = home + '/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'

# get latest modified date in target parth
targetfiles = glob.glob(targetpath+'*')
if targetfiles!=[]:
    latestfile = max(targetfiles, key=os.path.getmtime)
    # get time threshold
    timethreshold = os.path.getmtime(latestfile)
else:
    timethreshold = os.path.getctime(sourcepath)
# read in all file names excluding folders
sourcefiles = [f for f in listdir(sourcepath) if isfile(join(sourcepath, f))]
# get latest modified date in source, only for files > 200k
file_list = [x for x in sourcefiles if os.path.getsize(sourcepath+x)>200000 and os.path.getmtime(sourcepath+x)>timethreshold]

#copy files
if file_list != []:
    for file in file_list:
        # check if image is vertical
        img = Image.open(sourcepath+file)
        if img.width < img.height:
            copyfile(sourcepath+file, tagetvertical+file+'.jpg')
        else:
            copyfile(sourcepath+file, targetpath+file+'.jpg')

print(str(len(file_list))+' file copied.')
