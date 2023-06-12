import os
from exploratree import save_directory_tree_txt, save_directory_tree_yaml, save_all_full_path, pathOforigin

def exportAll(directory_path):
	output_folder = os.path.dirname(directory_path)+os.sep+'directory_tree_'+os.path.basename(directory_path)
	os.makedirs(output_folder, exist_ok=True)
	output_file = output_folder+os.sep+'directory_tree_'+os.path.basename(directory_path)
	save_directory_tree_txt(directory_path, output_file+'.txt')
	save_directory_tree_yaml(directory_path, output_file+'.yaml')
	save_all_full_path(directory_path, output_file+'_glob.txt')
	pathOforigin(directory_path, output_file+'_pathOfOrigin.txt')
	print(f"Directory tree saved to: \n {output_folder}")
	print('')
	print('')
	print('''The following file format have been eported: \n
		- yaml: this is useful to use exploratree to search for specific file \n
		- glob.txt: full output of the path \n
		- txt: when open with sublime text enable to navigate the text file like an actual directory collapsible etc.\n
		- _pathOfOrigin.txt: contains the original path of where the initial directory came from 
		''')

def main():
	print('')
	print('-------------------------------------------')
	tmpFol = input("Drag folder/directory to export the tree (a.k.a. directory structure) of and press Enter:")
	tmpFol = tmpFol.replace('\\','/')
	tmpFol = tmpFol.replace('"','')
	print('-------------------------------------------')
	print('')

	exportAll(tmpFol)


if __name__ == '__main__':
	main()