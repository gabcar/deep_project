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
    with open(train_label_path) as f:#change train/test
        f = filter(None, f)
        for line in f:
            temp  = line.rstrip()
            split_line = temp.split(',')

            #print split_line[0], split_line[1:]
            img = np.array(Image.open(train_image_folder + split_line[0])) #change train/test
            if len(img.shape) is 3:
                test_image_paths.append(split_line[0])
                test_labels.append(split_line[1:])

            else:
                count +=1
                #print 'image with shape: ', img.shape, ' removed.'

        #print len(test_image_paths)
        #print test_labels[0]
        #print np.array(test_labels).shape

        array_labels = np.array(test_labels)
        array_labels_trimmed = array_labels[:,0:3]
        no_of_f = array_labels_trimmed.shape[0]
        #print no_of_f
        new_labels = np.zeros((no_of_f,6))

        #print array_labels_trimmed[-1,:]
        temp = np.zeros(array_labels_trimmed.shape);
        for i,line in enumerate(array_labels_trimmed):
            temp_line = np.array(map(int,line))
            temp_line = temp_line -1
            #print temp_line
            for j,num in enumerate(temp_line):
                #print j
                if num == 0:
                    new_labels[i,2*j] = 1
                else:
                    new_labels[i,2*j+1] = 1
        #print new_labels[-1,:]



        #create the files
        for rownum,line in enumerate(test_image_paths):
            file_labels = open('pre_proc/ver2/train/' + line + '.txt','w')
            for i in new_labels[rownum]:
                file_labels.write(str(int(i)) + '\n')
            file_labels.close()
        #print len(test_image_list),len(test_labels)

read_data(path)
