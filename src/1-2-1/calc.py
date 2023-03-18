import os
import pathlib
import subprocess

print("---enter calc.py---")

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
