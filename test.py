import os 

dir_path = os.getcwd()
folderName = 'numbers'
path = os.path.join(dir_path, folderName)
os.mkdir(path)