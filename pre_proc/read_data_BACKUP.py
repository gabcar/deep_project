import sys
from PIL import Image
import glob
import numpy as np


path = sys.argv[1]
print path

"""
Reads data and converts labels to one hot representation

path: path to the data and labels. in format:
PATH/test_labels.txt, PATH/training_labels.txt., PATH/test_data/, PATH/trainig_data/
"""

def read_data(path):
    test_image_list=[]
    training_labels=[]
    test_labels=[]
    training_labels=[]

    test_image_folder = path + 'test_data/'
    train_image_folder = path + 'training_data/'
    test_label_path = path + 'test_labels.txt'
    train_label_path= path + 'training_labels.txt'
    count = 0
    test_image_paths = []
    with open(test_label_path) as f:
        f = filter(None, f)
        for line in f:
            temp  = line.rstrip()
            split_line = temp.split(',')


            #print split_line[0], split_line[1:]
            img = np.array(Image.open(test_image_folder + split_line[0]))
            if len(img.shape) is 3:
                test_image_paths.append(split_line[0])
                test_labels.append(split_line[1:])

            else:
                count +=1
                print 'image with shape: ', img.shape, ' removed.'

        print len(test_image_paths)
        print test_labels[-1]

        #create the files
        """
        for rownum,line in enumerate(test_image_paths):
            file_labels = open('pre_proc/train/' + line + '.txt','w')
            for i in test_labels[rownum]:
                file_labels.write(i + '\n')
            file_labels.close()
        print len(test_image_list),len(test_labels)
        """




read_data(path)
