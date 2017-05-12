import shutil
import sys
import os

source= sys.argv[1]
label_txt_name = sys.argv[2]
destination = sys.argv[3]

training_file = open(label_txt_name,'r')




if not os.path.exists(destination + '/male'):
    os.makedirs(destination + '/male')
if not os.path.exists(destination + '/female'):
    os.makedirs(destination + '/female')
if not os.path.exists(destination + '/glasses'):
    os.makedirs(destination + '/glasses')
if not os.path.exists(destination + '/glasses'):
    os.makedirs(destination + '/glasses')
if not os.path.exists(destination + '/no_glasses'):
    os.makedirs(destination + '/no_glasses')
if not os.path.exists(destination + '/no_smiling'):
    os.makedirs(destination + '/no_smiling')
if not os.path.exists(destination + '/smiling'):
    os.makedirs(destination + '/smiling')

i = 1
for line in training_file:
	line_list = line.split(',')
	#line = training_file.readline()
	if line_list[1] == '1':
		shutil.copy(source + line_list[0],destination + '/male/')
	if line_list[1] == '2':
		shutil.copy(source + line_list[0],destination + '/female/')
	if line_list[3] == '1':
		shutil.copy(source + line_list[0],destination + '/glasses/')
	if line_list[3] == '2':
		shutil.copy(source + line_list[0],destination + '/no_glasses/')
	if line_list[2] == '1':
		shutil.copy(source + line_list[0],destination + '/smiling/')
	if line_list[2] == '2':
		shutil.copy(source + line_list[0],destination + '/no_smiling/')

print 'Moved '+str(i)+' files'
