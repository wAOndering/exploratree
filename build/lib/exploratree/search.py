from exploratree import search_file, read_directory_tree_yaml
#from typing import Optional, Callable, List, Union, Text, TypeVar

def main():
	# def main(args: Optional[List] = None):
	print('')
	print('-------------------------------------------')
	yamlFile = input("Drag the yaml file that contains the directory (eg. directory_tree_*.yaml) press Enter:")
	yamlFile = yamlFile.replace('\\','/')
	yamlFile = yamlFile.replace('"','')
	print('-------------------------------------------')
	print('')
	dirTree = read_directory_tree_yaml(yamlFile)


	searchString = ''
	while searchString != 'q':
		# print('eller')
		print('')
		print('-------------------------------------------')
		print("Type the string to search within the directory press Enter:\nif no more item needs to be searched press q:\n")
		searchString = input('string to find: ')
		print('-------------------------------------------')
		print('')

		search_file(dirTree, searchString)

if __name__ == '__main__':
	main()