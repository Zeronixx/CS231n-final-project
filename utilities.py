import struct
import numpy as np
import csv
from skimage.transform import resize
from matplotlib import pyplot as plt


# Retrieves the associated image of a dataset, turns it into a numpy array, and returns it.
def getImage(data):
    barr = bytearray(data.PixelData)
    count = len(barr) // 2
    sarr = struct.unpack('H'*count, barr)
    return np.array(sarr).reshape([data.Rows, data.Columns])

# Displays the image associated with a dataset.
def showImage(arr):
    plt.imshow(arr, cmap="gray_r")
    plt.show()

#displays array of images each in their own figure
def showImages(imgarr) :

    for i in range(len(imgarr)) :
        plt.figure(i)
        plt.imshow(imgarr[i], cmap="gray_r")
        if i%10==0 :
            plt.show()
# Takes in an image (represented as np array), and resizes it to shape specified by dims.
def resizeImage(arr, dims):
    return resize(arr, dims, preserve_range=True)

def loadLabels():
    labels = dict()
    with open('/home/user1_team6/project/data/XRAbdomen_labels.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for line in r:
            accnum, label = line
            labels[accnum] = label
        return labels
                                                    
