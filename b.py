import subprocess

# Define the file path
file_path = "./challpub"

# Run the `file` command to determine the type of binary
file_info = subprocess.run(["file", file_path], capture_output=True, text=True).stdout

# Run the `strings` command to extract readable strings from the binary
strings_output = subprocess.run(["strings", "-a", file_path], capture_output=True, text=True).stdout

file_info, strings_output[:1000]  #
