import shutil

destination_male_with_glasses = '/Users/christianchamoun/Tensorflow-git/tensorflow/MTFL/Male_with_glasses'
destination_female_with_glasses = '/Users/christianchamoun/Tensorflow-git/tensorflow/MTFL/Female_with_glasses'
destination_male_without_glasses = '/Users/christianchamoun/Tensorflow-git/tensorflow/MTFL/Male_without_glasses'
destination_female_without_glasses = '/Users/christianchamoun/Tensorflow-git/tensorflow/MTFL/Female_without_glasses'
training_file = open('training.txt','r')
i = 1
for line in training_file:
	line_list = line.split(' ')
	source = '/Users/christianchamoun/Tensorflow-git/tensorflow/MTFL/'+str(line_list[0]).replace('\\','/')

	if line_list[11] == '1' and line_list[13] == '1':
		shutil.copy(source,destination_male_with_glasses)
	elif line_list[11] == '1' and line_list[13] == '2':
		shutil.copy(source,destination_male_without_glasses)
	elif line_list[11] == '2' and line_list[13] == '1':
		shutil.copy(source,destination_female_with_glasses)
	elif line_list[11] == '2' and line_list[13] == '2':
		shutil.copy(source,destination_female_without_glasses)
	else:
		print 'TRANSA!'
	
	i = i+1

print 'Moved '+str(i)+' files'