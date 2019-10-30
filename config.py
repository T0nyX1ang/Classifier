import argparse
import json
import os

def _validate_directory(directory):
	if type(directory) is not str: # whitelist constraint (string only)
		return False
	else:
		# the source should be a directory
		return os.path.isdir(directory)

def commit_changes(name, source, destination, extension, recursive):
	if not os.path.exists('config.json'):
		with open('config.json', 'w') as f:
			f.write(json.dumps({})) # dumps an empty JSON format

	with open('config.json', 'r') as f:
		jsin = json.loads(f.read())

	if name is None or name in jsin or not _validate_directory(source) or source == os.getcwd():
		print('A valid name and source directory should be provided.')
		return False
	else:
		jsin[name] = {}
		jsin[name]['source'] = source

	if destination is None:
		destination = os.path.join(source, name)
	elif not _validate_directory(destination):
		print('A valid destination directory should be provided.')
		return False

	if os.path.exists(destination):
		print('Warning: A folder with the same name is created before, consider changing a new name.')
	
	jsin[name]['destination'] = destination
	jsin[name]['extension'] = [] if extension is None else extension
	jsin[name]['recursive'] = recursive

	with open('config.json', 'w') as f:
		f.write(json.dumps(jsin, ensure_ascii=False, sort_keys=True, indent=4)) # generate JSON elegantly
	return True

parser = argparse.ArgumentParser(description='This file is used to make configurations.')
parser.add_argument('-n', '--name', type=str, help='Set the name of a single configuration.')
parser.add_argument('-s', '--source', type=str, help='Define the source folder to search your files.')
parser.add_argument('-d', '--destination', type=str, help='Define the target folder to put your files.')
parser.add_argument('-e', '--extension', nargs='*', help='Define the extensions to classify your files.')
parser.add_argument('-r', '--recursive', action='store_true', help='Enable recursive searching in folders.')
args = parser.parse_args()

if commit_changes(args.name, args.source, args.destination, args.extension, args.recursive):
	print('This configuration is successfully commited to the config.json.')
else:
	print('Fail to commit the configuration, please check your parameters.')