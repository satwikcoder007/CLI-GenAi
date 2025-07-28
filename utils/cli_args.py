
import argparse
import sys
from utils.context_utils import append_context_if_exists

def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--Prompt", help="Enter your prompt here", nargs='+')
    parser.add_argument("-mp", "--MultiPrompt", help="Enter your prompt here (multi-line via stdin)", nargs='?', const=True)
    parser.add_argument("-c", "--Context", help="Provide code file as context", nargs='+')
    args = parser.parse_args()

    # Handle prompt (single or multiline)
    task_instruction = "Instruction: "
    if args.MultiPrompt:
        print("👉 Paste your multi-line prompt. Press Ctrl+D (or Ctrl+Z on Windows) when done:\n")
        read = sys.stdin.read()
        task_instruction += read.strip()
    elif args.Prompt:
        read = ' '.join(args.Prompt)
        task_instruction += read.strip()
    else:
        print("❌ Please enter a prompt using -p or -mp.")
        sys.exit(0)

    # Handle context files
    file_metadata = {}
    if args.Context:
        for file in args.Context:
            file_metadata = append_context_if_exists(file)

    return file_metadata, task_instruction
