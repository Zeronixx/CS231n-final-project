import csv
import numpy as np

IN = "./data_nodupes/"
OUT = "./data_inverted/"

with open("labels.csv") as csvfile:
  reader = csv.reader(csvfile)
  for line in reader:

    i = line[0]
    mc = line[3]
    print("File {}, monochromaticity {}".format(i,mc))
    filename = "{}.npy".format(i)
    try:
      arr = np.load(IN + filename, mmap_mode='r')
    except:
      continue
    if mc == 2:
      arr = 2**16 - 1 - arr
    np.save(OUT + filename, arr)
  
