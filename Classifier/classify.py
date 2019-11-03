import os
import sys
import shutil
import time
import json
import hashlib
import argparse
import glob

parser = argparse.ArgumentParser(description='This file is used to make classfications.')
parser.add_argument('-s', '--source', help='Set source directory (files to move out).')
parser.add_argument('-d', '--destination', help='Set destination directory (files to move into).')
parser.add_argument('-b', '--blacklist', nargs='*', help='Set files/folders to be ignored. Regular expression is supported.')
parser.add_argument('-e', '--empty', action='store_true', help='Empty file deletion.')
parser.add_argument('-p', '--swipe', action='store_true', help='Swipe the empty folder after file moves.')
args = parser.parse_args()

# load configuration
working_path = os.path.split(os.path.realpath(__file__))[0] # making configurations into the same directory of this project
config_path = os.path.join(working_path, 'config.json')

if os.path.exists(config_path):
	with open(config_path, 'r') as f:
		fin = f.read() # read once
		config = json.loads(fin)
		hash_id = hashlib.md5(fin.encode('utf-8')).hexdigest()
	time_id = str(time.time())
	print('Configuration is loaded successfully.')
else:
	print('Please generate a configuration file first.')
	sys.exit()

if args.blacklist is None:
	blacklist = []
else:
	blacklist = args.blacklist
blacklist.append(os.path.split(os.path.realpath(__file__))[0]) # Append executing directory to blacklist

# Directory detection
if args.source is None or not os.path.isdir(args.source):
	print('A valid source directory must be applied.')
	sys.exit()
else:
	print('The source directory has been to set to:', args.source)

if os.path.isdir(args.destination):
	print('Destination folder is added to blacklist.')
	blacklist.append(os.path.realpath(args.destination))
else:
	print('Creating destination workspace:', args.destination)
	os.mkdir(args.destination)

folder_name = hash_id + '_' + time_id
dest_dir = os.path.join(args.destination, folder_name)
os.mkdir(dest_dir)
blacklist.append(dest_dir) # append the destination directory to the end of blacklist
# Folder creation
for extension in config:
	final_dir = os.path.join(dest_dir, config[extension])
	if not os.path.exists(final_dir):
		os.mkdir(final_dir)
os.mkdir(os.path.join(dest_dir, 'Others'))

def check_blacklist(filename):
	if filename in blacklist:
		return True
	for black in blacklist:
		if filename in glob.glob(black) or filename in glob.glob(os.path.join(args.source, black)):
			return True
	return False

# Classify
for filename in os.listdir(args.source):
	if os.path.realpath(args.source) in blacklist or check_blacklist(os.path.join(args.source, filename)):
		continue # blacklist detection
	filename = os.path.join(os.path.realpath(args.source), filename)
	if args.empty and os.path.getsize(filename) == 0 and os.path.isfile(filename):
		print('Removing empty file:', filename)
		os.remove(filename) # empty file deletion
		continue 
	if os.path.isfile(filename):
		filepath, extension = os.path.splitext(filename)
		extension = extension.replace('.', '').lower()
		if extension in config:
			shutil.move(filename, os.path.join(dest_dir, config[extension]))
		else:
			shutil.move(filename, os.path.join(dest_dir, 'Others'))
	else:
		if not os.path.isdir(os.path.join(dest_dir, os.path.split(filename)[-1])):
			shutil.move(filename, dest_dir)
		else:
			new_name = 'Duplication_' + time_id # Isolate duplicated folders
			os.mkdir(os.path.join(dest_dir, new_name))
			shutil.move(filename, os.path.join(dest_dir, new_name))

if args.swipe:
	if len(os.listdir(args.source)) > 0:
		print('The source folder is not empty, this action is harmful.')
		sys.exit()
	elif args.source == os.getcwd():
		print('You are into the source folder, please get out first.')
		sys.exit()
	else:
		print('Swiping the source folder.')
		os.rmdir(args.source)
