# Classifier
A simple classifier to manage your messy desktop files.

Under development now, preparing to archive these goals:

- [x] Configuration for extensions.
- [x] Merging folders & folder isolation.
- [ ] Regular expression searching (using a blacklist to block some files).
- [x] Source and target folder detection.
- [x] Symlink detection (especially on Windows).
- [ ] Mimetype switch (manage by mimetype).
- [ ] Python package generation.

## Usage:
* config.py:
```
usage: config.py [-h] [-n NAME] [-e [EXTENSION [EXTENSION ...]]] [-f] [-d]

This file is used to make configurations.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Set the name of a single extension set.
  -e [EXTENSION [EXTENSION ...]], --extension [EXTENSION [EXTENSION ...]]
                        Define the extensions to classify your files.
  -f, --force           Forcibly change the category of an extension.
  -d, --delete          Delete extensions.
```

* classify.py:
```
usage: classify.py [-h] [-s SOURCE] [-d DESTINATION]
                   [-b [BLACKLIST [BLACKLIST ...]]] [-e] [-p]

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

* merge.py:
```
usage: merge.py [-h] [-d DIRECTORY DIRECTORY]

This file is used to move files from a earlier folder to a newer folder.

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY DIRECTORY, --directory DIRECTORY DIRECTORY
                        Set the name of a single extension set.
```

## License:
* Under MIT License, see LICENSE for more details.
* Copyright (c) 2019 Tony Xiang.
