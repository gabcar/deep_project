import numpy as np
import tensorflow as tf
import glob
from PIL import Image

images=[]
labels=[] #load labels into list
with open('./Datasets/MTFL/testing.txt') as f:
    f = filter(None, f)
    for line in f:
        str_arr = [elt.strip() for elt in line.split(' ')]
        str_arr = filter(None,str_arr)
        if str_arr:
            piece_str = str_arr[0].replace('\\','/')
            file_name = './Datasets/MTFL/'+ piece_str
            im = Image.open(file_name)
            save_path = piece_str.split('/')[-1]
            im.save('./test_data/' + save_path, 'JPEG')
            #images.append(np.array(Image.open(file_name)).reshape(1,-1))
            labels.append(save_path+  ","+ str_arr[-4] +","+ str_arr[-3]+"," + str_arr[-2] +","+ str_arr[-1])
            #print "image appended: ", str_arr



text_file = open("test_labels.txt", "w")
for line in labels:
  text_file.write("%s\n" % line)
text_file.close()
