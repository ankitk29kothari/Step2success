from folder_operations import*
from text_file_function import*
import os.path
io_file = (os.path.dirname(__file__))


print(io_file)
create_folder('function_call')
append(file_name=io_file+'/function_call/new_file.txt',variable='Hi Iam a new file with folder')