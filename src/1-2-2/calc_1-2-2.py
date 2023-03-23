import os
import pathlib

print("---enter calc.py---")

training_dir = os.getenv("SM_CHANNEL_TRAINING")
for txt_file in pathlib.Path(str(training_dir)).glob("**/*.txt"):
    print(f"reading {str(txt_file)}...")
    with txt_file.open(mode="rt") as f:
        input_text_lines = f.read()
    print("---データの確認---")
    print(input_text_lines)
    print("---計算結果---")
    for input_text in input_text_lines.split("\n"):
        print(eval(input_text))

exit()
