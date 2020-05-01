import os, glob
def nested_count(folder_path, level=0):
    for folder in sorted(glob.glob('{}/'.format(os.path.join(folder_path, '*')))):
        print('{:}{:}: {:,}'.format('    '*level, os.path.split(os.path.split(folder)[-2])[-1], len(glob.glob(os.path.join(folder, '*')))))
        nested_count(folder, level+1)
nested_count('.') 