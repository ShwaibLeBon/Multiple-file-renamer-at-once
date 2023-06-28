import os

path = ""
folders = os.listdir(path)
file_path = ""

# For nested folders
for folder in folders:
	file_path = os.path.join(path, folder)
	files = os.listdir(file_path.replace("\\", '/'))

	print (file_path)
	for file in files:
		to_rename = file.replace(".fdmdownload", "")
		os.rename(os.path.join(file_path, file), os.path.join(file_path, to_rename))
