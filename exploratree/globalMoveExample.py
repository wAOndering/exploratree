'''
binArchived
'''
import glob
import shutil
import os
import tqdm

def copy_file_with_structure(src_file, dst_file, option='copy'):
    # Get the absolute path of the source file
    abs_src_file = os.path.abspath(src_file)

    # Create the destination directory if it doesn't exist
    dst_dir = os.path.dirname(dst_file)
    os.makedirs(dst_dir, exist_ok=True)

    # Copy the file to the destination directory, preserving the directory structure
    if option == 'copy':
    	shutil.copy2(abs_src_file, dst_file)
    elif option == 'move':
    	shutil.move(abs_src_file, dst_file)

## moving files around while retaining the strucuture
primaryFolder = r'Y:\Jessie\e3 - Data Analysis'
archivedFolder = r"Y:\Jessie\e3 - Data Analysis\e3 Data\binArchive"
files = set(glob.glob(primaryFolder+'/**/*.bin', recursive=True)) - set(glob.glob(archivedFolder+'/**/*.bin', recursive=True))

## could add a file of origin in a pandas file source file destination file might be easier to do the conversion the reverse way
for f in tqdm.tqdm(list(files)):
	print(f)
	fS = f.split(os.sep)
	fout = os.sep.join([archivedFolder]+fS[4:])
	copy_file_with_structure(f,fout,'move')
