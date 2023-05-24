# -*- coding: utf-8 -*-
# Purpose: build requirements.txt file

import subprocess


# Get a list of installed packages
installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')

# Write the list of packages to a requirements.txt file without version numbers
with open('requirements.txt', 'w') as f:
    for package in installed_packages:
        package_name = package.split('==')[0]
        f.write(package_name + '\n')