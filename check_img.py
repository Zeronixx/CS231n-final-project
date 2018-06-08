import imageio
from utilities import *

from skimage import io
import numpy as np
from os import listdir
from os.path import isfile, join
import warnings


mypath = './img_nodupes_removing/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()
onlyimgs = []

for f in onlyfiles:
    if f=="exceptions.txt" :
        continue

    onlyimgs.append(imageio.imread("img_nodupes/"+ f))

showImages(onlyimgs)
