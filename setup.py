#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import setuptools

# with open("README.md", encoding="utf-8", errors="replace") as fh:
#     long_description = fh.read()


# Setting up
setuptools.setup(
       # the name must match the folder name 'verysimplemodule'
        name="exploratree", 
        version="0.0.1",
        author="",
        author_email="vaissiere.t@ufl.edu",
        # description=DESCRIPTION,
        # long_description=LONG_DESCRIPTION,
        packages=setuptools.find_packages(),
        install_requires=["tqdm",
                          "pyyaml"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        entry_points={
            "console_scripts":[
            "exploratree-get=exploratree.directory_export:main", ## export the different directories
            "exploratree-fakeDir=exploratree.create_directory:main", ## create the fake directories to simulate or test the program
            "exploratree-search=exploratree.search:main"
            ]
        },
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
