# Example usage

## Create a fake tree
## random.seed is set so that this example is reproducible
root_directory = 'fake_directory'
depth = 2
num_files_per_directory = 2
create_fake_directory_structure(root_directory, depth, num_files_per_directory)
print(f"Fake directory structure created at: \n {os.getcwd()+os.sep+root_directory}")


## Export the tree for the folder of interest
directory_path = r'C:\Users\Windows\Desktop\fake_directory'
output_folder = os.path.dirname(directory_path)+os.sep+'directory_tree_'+os.path.basename(directory_path)
os.makedirs(output_folder, exist_ok=True)



## Load the yaml file
dir_yaml_path = r"C:\Users\Windows\Desktop\directory_tree_fake_directory\directory_tree_fake_directory.yaml"
dir_yaml = exploratree.read_directory_tree_yaml(dir_yaml_path)

## Example of directory search
string_to_find = 'bceh.t'
search_directory_tree(dir_yaml, string_to_find)


pathsList = [r'Y:\Randy\Macroscope Data\Cohort_1_May_to_July_2022',
			 r'Y:\Randy\Macroscope Data\Cohort_2_May_to_July_2023',
			 r'Y:\Diana\inscopix data\Sens\C5\recorded']

for i in tqdm.tqdm(pathsList):
	exportAll(i)


pathList = [r'Y:\Randy\Macroscope Data\directory_tree_Cohort_1_May_to_July_2022',
r'Y:\Randy\Macroscope Data\directory_tree_Cohort_2_May_to_July_2023',
r'Y:\Diana\inscopix data\Sens\C5\directory_tree_recorded']

for i in pathList:
	shutil.copytree(i, r'Y:\AZURE LAB ARCHIVE\Archived Trees')


import os
import shutil

source_dir = 'path/to/source_directory'  # Replace with the path of the source directory
destination_dir = 'path/to/destination_directory'  # Replace with the path of the destination directory

# Iterate over files in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        source_path = os.path.join(root, file)
        destination_path = os.path.join(destination_dir, file)

        # Copy the file to the destination directory
        shutil.copy2(source_path, destination_path)

print('Directory contents copied successfully.')