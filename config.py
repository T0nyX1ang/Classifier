import argparse
import json
import os
import sys

parser = argparse.ArgumentParser(description='This file is used to make configurations.')
parser.add_argument('-n', '--name', type=str, help='Set the name of a single extension set.')
parser.add_argument('-e', '--extension', nargs='*', help='Define the extensions to classify your files.')
parser.add_argument('-f', '--force', action='store_true', help='Forcibly change the category of an extension.')
args = parser.parse_args()

if not os.path.exists('config.json'):
	with open('config.json', 'w') as f:
		f.write(json.dumps({}))

with open('config.json', 'r') as f:
	config = json.loads(f.read())

# Setting the name
if args.name is None:
	print('A name should be given to describe the extension set.')
	sys.exit()

# Setting extension
extension = [] if args.extension is None else args.extension
for ext in extension:
	if ext not in config:
		config[ext] = args.name 
		print('Setting "%s" to "%s" category.' % (ext, args.name))
	elif args.force:
		config[ext] = args.name 
		print('Forcibly setting "%s" to "%s" category.' % (ext, args.name))		
	else:
		print('This extension "%s" has been configured before, ignoring it.' % ext)

with open('config.json', 'w') as f:
	f.write(json.dumps(config, indent=4))

print('The configuration is updated successfully.')