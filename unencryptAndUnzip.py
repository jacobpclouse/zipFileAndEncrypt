## Zip Files with Python
## https://www.geeksforgeeks.org/working-zip-files-python/

## Encrypt Files with Python
## https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
## For encryption to work, you need to 'pip install cryptography' 

# Note - when outputting a zip file, this will overwrite any pre exisiting files with the same name, be careful!
# make sure that this program is in the same folder as the key and file you want to unencrypt
# maybe add functionality where if the "filename.key" does not exist, then prompt for the key manually

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# importing required modules
# zipping modules
from msilib.schema import Directory
from zipfile import ZipFile
import os
# encryption modules
from cryptography.fernet import Fernet
# copying Files
import shutil
import os.path

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


# Decrypting and unzipping
def decrypt_zip_file(zip_file_name):

    # signal start of decryption
    print('Decrypting....')

    # opening the encrypted file
    with open(f'{zip_file_name}.zip', 'rb') as enc_file:
	    encrypted = enc_file.read()

    # opening the key file
    with open(f'{zip_file_name}.key', 'rb') as enc_key_file:
	    zip_key = enc_key_file.read()

    # using the key
    fernet = Fernet(zip_key)

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # removing 'encrypted_' prefix
    decrypted_file_name_out = zip_file_name[10:]

    # opening the file in write mode and writing the decrypted data
    with open(f'decrypted_{decrypted_file_name_out}.zip', 'wb') as dec_file:
	    dec_file.write(decrypted)

    # print out success decryption
    print('Zip File decrypted successfully!')


# ---


# Unzip function
def unzip_after_decrypt(what_decrypted_output_zip_is_named):

    # removing 'encrypted_' prefix, adding 'decrypted_' prefix
    unpack_decrypted_file_name_out = f'decrypted_{what_decrypted_output_zip_is_named[10:]}'

    # opening the zip file in READ mode
    with ZipFile(f'{unpack_decrypted_file_name_out}.zip', 'r') as zip:

        # printing all the contents of the zip file
        zip.printdir()
  
        # extracting all the files
        print('Unzipping....')
        zip.extractall()

    # print out success unzip
    print('Zip File unzipped successfully!')


# --


# Delete local files besides key and encrypted zip
#def clean_up_files(local_folder,zipped_folder):
def clean_up_files(zipped_folder):

    # removing 'encrypted_' prefix, adding 'decrypted_' prefix
    file_to_delete = f'decrypted_{zipped_folder[10:]}.zip'

    # delete zipped file 
    os.remove(file_to_delete)

    ##delete directory
    ##os.remove(local_folder)
    # can't delete local directory: permission denied

    # print out successful cleanup
    print('Cleanup Completed successfully!')

# --

# -=-=-=-=-=-=-=-
## Main Program
# -=-=-=-=-=-=-=-

def main():

    # for now, just get decrytion working and then worry about filepaths

    # having user enter zip file output name 
    # WITH the 'encrypted_' prefex before, the original name of the file
    what_output_zip_is_named = input('What is the encrypted Zip called? (DO NOT INCLUDE .zip at the end): ')  

    # executing decryption function
    decrypt_zip_file(what_output_zip_is_named)

    # unzipping decrypted zip file
    unzip_after_decrypt(what_output_zip_is_named)

    # clean up zip after decrypt
    clean_up_files(what_output_zip_is_named)

if __name__ == "__main__":
	main()
