import shutil

training_file = open('training.txt','r')
i = 1
for line in training_file:
	line_list = line.split(' ')
	#line = training_file.readline()
	source = '/Users/christianchamoun/MTFL/'+str(line_list[0]).replace('\\','/')	
	destination_male = '/Users/christianchamoun/MTFL/Male'
	destination_female = '/Users/christianchamoun/MTFL/Female'

	if line_list[11] == '1':
		shutil.move(source,destination_male)
	elif line_list[11] == '2':
		shutil.move(source,destination_female)
	else:
		print 'TRANSA!'
	
	i = i+1

print 'Moved '+str(i)+' files'