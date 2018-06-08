import pydicom

with open('full_paths.txt', 'r') as file:
  for line in file:
    if line[-1] == "\n": line = line[:-1]
    dcm = pydicom.dcmread(line)

    print(dcm.Modality)
