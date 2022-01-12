


def create_folder(directory):
	import os
	if not os.path.exists(directory):
		os.makedirs(directory)
		print("created")
	else:
		print("already created")

#for i in range(1,10):
#	create_folder(str(i))



def delete(directory):
	# when folder is empty
	import os
	os.rmdir(directory)
	print(directory+' deleted')


def delete_dir(directory):
	#any time
	import shutil
	shutil.rmtree(directory)
	print(directory+' deleted')

def delete_file(file_name):
	#any time
	import os
	os.remove(file_name)
	print(file_name+' deleted')



#for i in range(2,1000,2):
#	delete_dir(r'C:\Users\mcjp2518\Desktop\step2successs\Python\file_handling\demoby_python\{}'.format(i))


































