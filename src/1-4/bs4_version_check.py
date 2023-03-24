import os
import subprocess

import bs4
import my_module
from nested_module import my_nested_module

print("---enter bs4_version_check.py---")

# check current directry
print(os.getcwd())  # /opt/ml/code
cp = subprocess.run("ls", capture_output=True)
print(cp.stdout)
# __init__.py
# bs4_version_check.py
# my_module.py
# nested_module
# requirements.txt

my_module.version_check(bs4)
my_nested_module.version_check(bs4)
exit()
