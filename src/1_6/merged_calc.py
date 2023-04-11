import argparse
import os
import pathlib
import subprocess

import bs4
import my_second_module as my_module
import torch

print("---enter calc.py---")

print("---parse args---")
parser = argparse.ArgumentParser()
parser.add_argument("--first_num", type=int)
parser.add_argument("--second_num", type=int)
parser.add_argument("--operator", type=str)
parser.add_argument("--model_dir", type=str)
args = parser.parse_args()
print(args)


print("---version check---")
my_module.version_check(bs4)
my_module.version_check(torch)
print(f"torch.cuda.is_available(): {torch.cuda.is_available()}")


# check under /opt
cp = subprocess.run(["ls", "-la", "/opt"], capture_output=True)
print(cp.stdout)
# aws
# conda
# ml

# check under /opt/ml
cp = subprocess.run(["ls", "-la", "/opt/ml"], capture_output=True)
print(cp.stdout)
# drwxr-xr-x 2 root root   21 Mar 23 12:34 code
# drwxr-xr-x 2 root root 4096 Mar 23 12:33 errors
# drwxr-xr-x 4 root root 4096 Mar 23 12:33 input
# drwxr-xr-x 2 root root 4096 Mar 23 12:33 model
# drwxr-xr-x 6 root root 4096 Mar 23 12:34 output

# check current directry
print(os.getcwd())  # /opt/ml/code
cp = subprocess.run("ls", capture_output=True)
print(cp.stdout)  # b'calc.py\n'

# check env variable
training_dir = os.getenv("SM_CHANNEL_TRAINING")
print(training_dir)  # /opt/ml/input/data/training
cp = subprocess.run(["ls", f"{training_dir}"], capture_output=True)
print(cp.stdout)  # b'calc.txt\n'

# data is placed under:
# /opt/ml/input/data/training/calc.txt

data_path = pathlib.Path(str(training_dir)) / "calc.txt"
with data_path.open(mode="rt") as f:
    input_text_lines = f.read()
print("---データの確認---")
print(input_text_lines)
print("---計算結果---")
for input_text in input_text_lines.split("\n"):
    print(eval(input_text))
