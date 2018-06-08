from skimage import io
import numpy as np
from os import listdir
from os.path import isfile, join
import os

import warnings

from PIL import Image
import subprocess


mypath = './img_nodupes_removing/'
viewable = './img_nodupes_viewable/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()

for name in onlyfiles :

    img = Image.open(viewable+name)
    while True :
        answer = input("Keep " + name + " (y/n or enter)? ") or "";
        img.show()
        if answer =="" :
            break
        elif answer=="no" or answer=="n" :
            os.remove(mypath+name)
            print("Removed: "+mypath+name)
            break
