# Classifier
A simple classifier to manage your messy desktop files.

Under development now, preparing to archive these goals:

- [x] Configuration for files' extensions. 
- [ ] Regular expression searching (using a blacklist to block some files).
- [x] Source and target folder detection.
- [x] Symlink detection (especially on Windows).
- [ ] Mimetype switch (manage by mimetype).
- [ ] Python package generation.

## Usage:
* config.py:
```
This file is used to make configurations.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Set the name of a single extension set.
  -e [EXTENSION [EXTENSION ...]], --extension [EXTENSION [EXTENSION ...]]
                        Define the extensions to classify your files.
  -f, --force           Forcibly change the category of an extension.
```
* classify.py:
```
This file is used to make classfications.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Setting source directory (files to move out).
  -d DESTINATION, --destination DESTINATION
                        Setting destination directory (files to move into).
  -b [BLACKLIST [BLACKLIST ...]], --blacklist [BLACKLIST [BLACKLIST ...]]
                        Setting files/folders to be ignored.
  -e, --empty           Empty file deletion.
  -p, --swipe           Swipe the empty folder after file moves.
```
* The folder merging feature is under development.

## License:
* Under MIT License, see LICENSE for more details.
* Copyright (c) 2019 Tony Xiang.
