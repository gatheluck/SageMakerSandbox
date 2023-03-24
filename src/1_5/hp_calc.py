import argparse
import json
import os

# Option 1: use argparse
print("Option 1")
parser = argparse.ArgumentParser()
parser.add_argument("--first_num", type=int)
parser.add_argument("--second_num", type=int)
parser.add_argument("--operator", type=str)
parser.add_argument("--model_dir", type=str)
args = parser.parse_args()
print(args)
# Namespace(first_num=5, model_dir=None, operator='m', second_num=2)

if args.operator == "p":
    print(f"The answer is {args.first_num + args.second_num}")
elif args.operator == "m":
    print(f"The answer is {args.first_num - args.second_num}")

# Option 2: load from environmental variable
print("Option 2")
hps = json.loads(os.getenv("SM_HPS"))  # type: ignore
print(hps)
# {'first_num': 5, 'operator': 'm', 'second_num': 2}

if hps["operator"] == "p":
    answer = hps["first_num"] + hps["second_num"]
    print(f"The answer is {answer}")
elif hps["operator"] == "m":
    answer = hps["first_num"] - hps["second_num"]
    print(f"The answer is {answer}")

exit()
