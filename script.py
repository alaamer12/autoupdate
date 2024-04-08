import sys
import json
import os

# Get the selected file or directory path from the command-line argument
selected_path = os.path.abspath(sys.argv[1])
print(sys.argv)
for path in sys.argv:
    print(path)

# Print the selected path
print(selected_path)

# Load existing paths from path.json or create an empty list
try:
    with open("path.json", "r") as f:
        paths = json.load(f)
except FileNotFoundError:
    paths = []

# Add the selected path to the list
paths.append(selected_path)

# Save the updated list back to path.json
with open("path.json", "w") as f:
    json.dump(paths, f, indent=4)

x = input("Press any key to continue...")
# TODO: Encode and decode paths for UTF-8
