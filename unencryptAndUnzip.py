## Zip Files with Python
## https://www.geeksforgeeks.org/working-zip-files-python/

## Encrypt Files with Python
## https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
## For encryption to work, you need to 'pip install cryptography' 

# Note - when outputting a zip file, this will overwrite any pre exisiting files with the same name, be careful!

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# importing required modules
# zipping modules
from msilib.schema import Directory
from zipfile import ZipFile
import os
# encryption modules
from cryptography.fernet import Fernet


# -=-=-=-=-=-=-=-
## Functions
# -=-=-=-=-=-=-=-
