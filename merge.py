import argparse
import os
import sys
import shutil

parser = argparse.ArgumentParser(description='This file is used to move files from a earlier folder to a newer folder.')
parser.add_argument('-d', '--directory', type=str, help='Set the name of a base directory to merge.')
parser.add_argument('-r', '--reverse', action='store_true', help='Reverse the order of folders in the directory.')
args = parser.parse_args()

if (args.directory is None):
	print('Two directories must be applied.')
	sys.exit()
elif not os.path.isdir(args.directory):
	print('A valid source directory must be applied.')
	sys.exit()
else:
	base_directory = os.path.realpath(args.directory)
	directory_list = os.listdir(base_directory)
	if args.reverse:
		directory_list.reverse()
	gather_folder = {}
	for folder in directory_list:
		try:
			hash_id, time_id = folder.split('_')
			if len(hash_id) != 32:
				print('Invalid hash length, please check your folder.')
				continue
		except Exception as e:
			print('Ignoring this folder, format should be [hash_id]_[time_id]')
			continue
		if hash_id in gather_folder:
			gather_folder[hash_id].append(os.path.join(base_directory, folder))
		else:
			gather_folder[hash_id] = [os.path.join(base_directory, folder)]	

	for hash_id in gather_folder:
		current_hash = gather_folder[hash_id]
		destination = current_hash[0]
		for foldername in current_hash[1:]:
			source = foldername
			time_id = (os.path.split(foldername)[-1]).split('_')[1]
			for foldername in os.listdir(source):
				if foldername not in os.listdir(destination):
					shutil.move(os.path.join(source, foldername), destination) # safely move because the destination doesn't have the folder
				else:
					for filename in os.listdir(os.path.join(source, foldername)):
						if filename not in os.listdir(os.path.join(destination, foldername)):
							# safely move because the destination folder doesn't have the file
							shutil.move(os.path.join(os.path.join(source, foldername), filename), os.path.join(destination, foldername))
						else:
							# rename the file with its timestamp
							new_name = os.path.join(os.path.join(destination, foldername), str(time_id) + '_' + filename)
							shutil.move(os.path.join(os.path.join(source, foldername), filename), new_name)
			shutil.rmtree(source) # remove the source folder			
