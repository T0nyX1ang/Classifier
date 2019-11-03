import argparse
import json
import os
import sys

parser = argparse.ArgumentParser(description='This file is used to make configurations.')
parser.add_argument('-n', '--name', type=str, help='Set the name of a single extension set.')
parser.add_argument('-e', '--extension', nargs='*', help='Define the extensions to classify your files.')
parser.add_argument('-f', '--force', action='store_true', help='Forcibly change the category of an extension.')
parser.add_argument('-d', '--delete', action='store_true', help='Delete extensions.')
args = parser.parse_args()

working_path = os.path.split(os.path.realpath(__file__))[0] # making configurations into the same directory of this project
config_path = os.path.join(working_path, 'config.json')

if not os.path.exists(config_path):
	with open(config_path, 'w') as f:
		f.write(json.dumps({}))

with open(config_path, 'r') as f:
	config = json.loads(f.read())

# Setting the name
if not args.delete and (args.name is None or args.name == 'Others'):
	print('A name should be given to describe the extension set, and it should not be "Others".')
	sys.exit()

# Setting extension
extension = [] if args.extension is None else args.extension
for ext in extension:
	if ext not in config:
		config[ext] = args.name 
		print('Setting "%s" to "%s" category.' % (ext, args.name))
	elif args.delete:
		config.pop(ext)
		print('Deleting extension:', ext)
	elif args.force:
		config[ext] = args.name 
		print('Forcibly setting "%s" to "%s" category.' % (ext, args.name))		
	else:
		print('This extension "%s" has been configured before, ignoring it.' % ext)

with open(config_path, 'w') as f:
	f.write(json.dumps(config, indent=4))

print('The configuration is updated successfully.')