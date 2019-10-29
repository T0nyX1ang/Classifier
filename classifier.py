# classfier.py
# a simple classifier for desktop files.
# Copyright (C) 2019 Tony Xiang
# Under MIT License.

import os, shutil, time

# Source directory and target direction configuration
SOURCE_DIR = os.getcwd()
TARGET_DIR = os.path.join(os.getcwd(), 'Classify')

print(TARGET_DIR)

# include more extension here is acceptable
FILE_TABLE = {
	'Documents': ('txt', 'pdf', 'dvi', 'ps', ),
	'MS-Word': ('doc', 'docx', 'rtf', ),
	'MS-Excel': ('xls', 'xlsx', ),
	'MS-Powerpoint': ('ppt', 'pptx', ),
	'Images': ('bmp', 'jpg', 'jpeg', 'gif', 'png', 'tif', 'tiff', 'ico', ),
	'Music': ('wav', 'flac', 'ape', 'mp3', ),
	'Movies': ('mp4', 'mkv', 'avi', 'ts', ),
	'Executables': ('exe', 'lnk'), 
	'Programming': ('html', 'css', 'c', 'cpp', 'cs', 'm', 'mat', 'r', 'py', 'java', 'js', 'tex', 'cls', 'rb', 'lua', 'json'),
	'Zipped': ('zip', 'rar', '7z', 'gz', 'tar', ),
}

# Empty file delection
DELECT_EMPTY = False

def prepare():
	if not os.path.exists(TARGET_DIR):
		os.mkdir(TARGET_DIR)
	for val in FILE_TABLE:
		dirs = os.path.join(TARGET_DIR, val)
		if not os.path.exists(dirs):
			os.mkdir(dirs)
	other = os.path.join(TARGET_DIR, 'Others')
	if not os.path.exists(other):
		os.mkdir(other)

def find_type(extension):
	for val in FILE_TABLE:
		if extension in FILE_TABLE[val]:
			return val
	return 'Others'

def classify():
	for filename in os.listdir(SOURCE_DIR):
		if filename == 'Classify' or filename == 'classifier.py':
			continue # skip the target directory
		is_directory = os.path.isdir(filename)
		if not is_directory:
			# deal with a single file
			extension = filename.split('.')[-1]
			filesize = os.path.getsize(filename)
			if (filesize == 0 and DELECT_EMPTY):
				print('Removing empty file:', filename)
				os.remove(filename)
			else:
				filepath = os.path.join(TARGET_DIR, find_type(extension.lower()))
				dirs = os.path.join(filepath, filename)
				if os.path.exists(dirs):
					dirs = filepath + filename[:-1] + str(time.time()) + extension
				shutil.move(filename, dirs)
		else:
			# deal with a directory
			dirs = os.path.join(TARGET_DIR, filename)
			if os.path.exists(dirs):
				dirs = dirs + '_' + str(time.time())
			shutil.move(filename, dirs)

if __name__ == '__main__':
	prepare()
	classify()