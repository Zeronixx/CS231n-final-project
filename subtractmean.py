from skimage import io
import numpy as np
from os import listdir
from os.path import isfile, join
import os

import warnings

from PIL import Image
import subprocess
from scipy import misc


mypath ="./data_relabelled_removed/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()

images = []
for name in onlyfiles :
    if name =="exceptions.txt" or name=="labels.csv":
        continue
    img = np.load(mypath+name)
    images.append(img)


        
total = np.zeros( (len(images), 3, 224,224))

for i in range(len(images)) :
    total[i] = images[i]

mean = np.mean(total, dtype="uint16")

for j in range(len(images)) :
    img = images[i]
    img-=mean
    np.save(mypath+onlyfiles[i], img)    
  
