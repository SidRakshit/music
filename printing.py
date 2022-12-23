import os
import pandas as pd
import numpy as np
import h5py
path = './MillionSongSubset'

fname = []

for root,d_names,f_names in os.walk(path):
    for f in f_names:
        fname.append(os.path.join(root, f))
    # print(root)
subset = fname[:20]
#print(subset)
#print("fname = %s" %fname[:10])

with h5py.File(subset[3], 'r') as hdf:
    ls = list(hdf.keys())
    print('List of datasets in this file: \n', ls)
    data = hdf.get('analysis')
    dataset1 = np.array(data)
    print(data)
    print(dataset1)
    print(dataset1.shape)

with h5py.File(subset[5], 'r') as hdf:
    ls = list(hdf.keys())
    print('List of datasets in this file: \n', ls)
    data1 = hdf.get('analysis')
    data2 = hdf.get('metadata')
    data3 = hdf.get('musicbrainz')
    dataset1 = np.array(data1)
    dataset2 = np.array(data2)
    dataset3 = np.array(data3)

    print(dataset1)
    print(dataset1.shape)
    print(dataset2)
    print(dataset2.shape)
    print(dataset3)
    print(dataset3.shape)
    print(type(dataset1))
