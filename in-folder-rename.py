import os

path = ""
files = os.listdir(path)

for file in files:
	# replace existing name with new one
	to_rename = file.replace("", "")
	os.rename(os.path.join(path, file), os.path.join(path, to_rename))
