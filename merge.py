import argparse
import os
import sys
import shutil

parser = argparse.ArgumentParser(description='This file is used to move files from a earlier folder to a newer folder.')
parser.add_argument('-d', '--directory', nargs=2, type=str, help='Set the name of a single extension set.')
args = parser.parse_args()

if (args.directory is None):
	print('Two directories must be applied.')
	sys.exit()
elif not os.path.isdir(args.directory[0]) or not os.path.isdir(args.directory[1]):
	print('A valid source directory must be applied.')
	sys.exit()
else:
	hash_1, time_1 = (os.path.split(args.directory[0])[-1]).split('_')
	hash_2, time_2 = (os.path.split(args.directory[1])[-1]).split('_')
	if hash_1 != hash_2:
		print('Unmatched hash, please ensure you use the same configuration.')
		sys.exit()
	else:
		source, destination = (args.directory[0],  args.directory[1]) if time_1 < time_2 else (args.directory[1], args.directory[0])
		time_id = min(time_1, time_2)
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
