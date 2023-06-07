from exploratree import create_fake_directory_structure
import os 
#from typing import Optional, Callable, List, Union, Text, TypeVar

def main():
	# def main(args: Optional[List] = None):
	## could implement parser option
	## see example https://github.com/talmolab/sleap/blob/develop/sleap/nn/inference.py
	## see example https://github.com/talmolab/sleap/blob/develop/setup.py

	# Example usage
	root_directory = 'fake_directory'
	depth = 2
	num_files_per_directory = 2

	os.chdir(os.path.dirname(os.getcwd()))
	create_fake_directory_structure(root_directory, depth, num_files_per_directory)
	print(f"Fake directory structure created at: \n {os.getcwd()+os.sep+root_directory}")

if __name__ == '__main__':
	main()