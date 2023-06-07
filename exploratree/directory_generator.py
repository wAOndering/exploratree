import os
import random
import string

def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_fake_directory_structure(root_directory, depth, num_files_per_directory):
    random.seed(8)
    os.makedirs(root_directory, exist_ok=True)

    if depth == 0:
        for i in range(num_files_per_directory):
            file_name = generate_random_name(5) + '.txt'
            file_path = os.path.join(root_directory, file_name)

            with open(file_path, 'w') as file:
                file.write('This is a fake text file.')

    else:
        for i in range(num_files_per_directory):
            directory_name = generate_random_name(8)
            directory_path = os.path.join(root_directory, directory_name)
            os.makedirs(directory_path, exist_ok=True)

            create_fake_directory_structure(directory_path, depth - 1, num_files_per_directory)
