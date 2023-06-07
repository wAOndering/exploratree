import os
import yaml
import glob
import tqdm


######### --- TXT file output
def save_directory_tree_txt(directory_path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(directory_path):
            level = root.replace(directory_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            file.write('{}{}\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file_name in files:
                file.write('{}{}\n'.format(subindent, file_name))

######### --- YAML file output
def build_directory_tree_yaml(directory_path):
    directory_tree = {'name': os.path.basename(directory_path), 'children': []}

    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        if os.path.isdir(entry_path):
            directory_tree['children'].append(build_directory_tree_yaml(entry_path))
        else:
            directory_tree['children'].append({'name': entry})

    return directory_tree

def save_directory_tree_yaml(directory_path, output_file):
    directory_tree = build_directory_tree_yaml(directory_path)

    with open(output_file, 'w') as file:
        yaml.dump(directory_tree, file)

def read_directory_tree_yaml(input_file):
    with open(input_file, 'r') as file:
        directory_tree = yaml.safe_load(file)
    return directory_tree

######### --- GLOB file output
def save_all_full_path(directory_path, output_file):
    file_export = glob.glob(directory_path+os.sep+'**/*',recursive=True)
    with open(output_file, 'w') as file:
        for item in file_export:
            file.write(str(item) + '\n')

######### --- search files
def search_file(tree, search_string, current_path=''):
    if 'name' in tree:
        current_path = os.path.join(current_path, tree['name'])
        if search_string in tree['name']:
            print("Found:", current_path)
    if 'children' in tree:
        for child in tree['children']:
            search_file(child, search_string, current_path)

######### --- get the path of origin
def pathOforigin(directory_path, output_file):
    with open(output_file, 'w') as file:
        file.write(directory_path)