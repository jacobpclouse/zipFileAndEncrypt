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

# Getting File paths function
def get_all_file_paths(inputDirectory):

	# initializing empty file paths list
	file_paths = []

	# crawling through directory and subdirectories
	for root, directories, files in os.walk(inputDirectory):
		for filename in files:
			# join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	# returning all file paths
	return file_paths		


# -- 


# Creating and writing to zip file function
def create_zip_file(zip_file_output_name, input_file_paths):

    # writing files to a zipfile
    with ZipFile(f"{zip_file_output_name}.zip",'w') as zip:
        # writing each file one by one
        for file in input_file_paths:
            zip.write(file)

    # print out success zip
    print('All files zipped successfully!')


# --


# creating key and writing it to a file
def create_key(zip_file_output_name_key):

    # key generation
    key = Fernet.generate_key()
  
    # string the key in a file
    with open(f'{zip_file_output_name_key}.key', 'wb') as filekey:
        filekey.write(key)

    # print out success key creation
    print('Key created successfully!')

# --


# encrypt file with previously generated key
# need to pass the prexisiting user filename var to this function
def encrypt_zip_with_key(zip_file_output_name_for_encryption):

    # signal start of encryption
    print('Encrypting....')

    # opening the key
    with open(f'{zip_file_output_name_for_encryption}.key', 'rb') as filekey:
        key = filekey.read()
  
    # using the generated key
    fernet = Fernet(key)
  
    # opening the original file to encrypt
    # make sure that you are just getting the file name WITHOUT the '.zip' extension at the end
    with open(f'{zip_file_output_name_for_encryption}.zip', 'rb') as file:
        original = file.read()
      
    # encrypting the file
    encrypted = fernet.encrypt(original)
  
    # opening the file in write mode and 
    # writing the encrypted data
    with open(f'encrypted_{zip_file_output_name_for_encryption}.zip', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    # print out success encryption
    print('Zip File encrypted successfully!')


# --


# -=-=-=-=-=-=-=-
## Variables
# -=-=-=-=-=-=-=-


# -=-=-=-=-=-=-=-
## Main Program
# -=-=-=-=-=-=-=-

def main():
	# path to folder which needs to be zipped
    # NEED TO GIVE FULL PATH or HAVE PROGRAM IN THE SAME DIRECTORY AS THE PYTHON PROGRAM
    ## do NOT use full path unless you want it to store every folder along the way, need to have the program cd into last folder location then extract it
    directory = input('EnterPath: ')

	# calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

	# printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
	    print(file_name)

    # having user enter zip file output name 
    what_output_zip_is_named = input('What will the output Zip be called? (THIS WILL OVERWRITE ANY ZIPS WITH THE SAME NAME!!): ')  

    # calling zip function to create zip file with previous variables
    create_zip_file(what_output_zip_is_named,file_paths)

    # creating key for encryption
    create_key(what_output_zip_is_named)

    # encrypting zip file
    encrypt_zip_with_key(what_output_zip_is_named)

if __name__ == "__main__":
	main()
