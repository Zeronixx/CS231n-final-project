from skimage import io, img_as_ubyte
import numpy as np
from os import listdir
from os.path import isfile, join
from utilities import *
import warnings
import png

mypath = './data_relabelled/'
outputdir = './img_nodupes_test'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    io.use_plugin('freeimage')

    for f in onlyfiles:
        if f=="labels.csv": continue
        with open("{}/exceptions.txt".format(outputdir), 'w') as exceptfile:
          
            print("Loading image: {}".format(f))
            arr = np.load(mypath+ f, mmap_mode='r')
            try:
                io.imsave('{}/{}.png'.format(outputdir, f[:-4]), arr)
                #with open('{}/{}.png'.format(outputdir, f[:-4]), 'wb') as pngfile:
                #    writer = png.Writer(width=arr.shape[1], height=arr.shape[0], bitdepth=16, greyscale=True)
                #    arr2list = arr.tolist()
                #    writer.write(pngfile, arr2list)
            except:
                err_msg = "Error when converting file {}. File not processed.".format(f)
                print(err_msg)
                exceptfile.write(err_msg + "\n")

