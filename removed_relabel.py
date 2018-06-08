import csv
import numpy as np

oldID2newID = dict()

IN_DIR = "data_nodupes_removed/"
OUT_DIR = "data_relabelled_removed/"

with open("files", 'r') as infile:
    for i, line in enumerate(infile):
        if line[-1] == "\n":
            line = line[:-1]
        file_name = line.split('/')[1] # xx.npy
        index = file_name.split(".")[0] # xx
        arr = np.load(line)
        oldID2newID[index] = i
     
        out_path = OUT_DIR + str(i) + ".npy"
        print("Saving file {} to file {}".format(line, out_path))
        np.save(out_path, arr) 

with open(IN_DIR + "labels.csv", 'r') as infile:
    reader = csv.reader(infile)
    with open(OUT_DIR + "labels.csv", 'w') as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            index = line[0]
            label = line[1]
            if index not in oldID2newID: continue
            i = oldID2newID[index]
            print("Mapping old label {} to new label {}".format(index, i))
            writer.writerow([i, label])

