import os
folders = input("enter the folders names with spaces: ").split()
for folder in folders:
    try:
        files = os.listdir(folder)
        print(f"Listing files for the {folder}: {files} \n")
    except FileNotFoundError:
        print(f"Please provide a valid folder name, {folder} does not exist")
        break
    
