from skimage import io
import numpy as np
from os import listdir
from os.path import isfile, join
import os

import warnings

from PIL import Image
import subprocess
from scipy import misc

mypath = './img_nodupes_removing/'
viewable = './img_nodupes_viewable/'
outputdir ="./data_nodupes_removed/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()

for name in onlyfiles :
    if name =="exceptions.txt" :
        continue
    img = misc.imread(viewable+name)
    np.save(outputdir+name.split(".")[0], img)
        
                                                                            
