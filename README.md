# Classifier
A simple classifier to manage your messy desktop files.

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
                        Set source directory (files to move out).
  -d DESTINATION, --destination DESTINATION
                        Set destination directory (files to move into).
  -b [BLACKLIST [BLACKLIST ...]], --blacklist [BLACKLIST [BLACKLIST ...]]
                        Set files/folders to be ignored. Regular expression is
                        supported.
  -e, --empty           Empty file deletion.
  -p, --swipe           Swipe the empty folder after file moves.
```

* merge.py:
```
usage: merge.py [-h] [-d DIRECTORY] [-r]

This file is used to merge folders based on their created time.

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Set the name of a base directory to merge.
  -r, --reverse         Reverse the order of folders in the directory.
```

## License:
* Under MIT License, see LICENSE for more details.
* Copyright (c) 2019 Tony Xiang.
