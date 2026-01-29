import os
from pathlib import Path

def create_folder():
    try:
        name = input("Please enter name of your folder: ")
        p = Path(name)
        p.mkdir() 
        print("Folder created successfully! ✅")
    except Exception as err:
        print(f"Sorry an error occured as {err}")
        
def read_file_folder():
    p = Path("")
    items = list(p.rglob("*"))
    for index, item in enumerate(items):
        print(f"{index+1}. {item}")
    
def update_folder():
    try:
        read_file_folder()
        old_name = input("Please tell which folder you want to update: ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Please tell your new folder name: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your folder name was updated successfully! ✅")
    except Exception as err:
        print(f"Sorry an error occured as {err}")
        

print("Options : ")

print("1. Create a folder")
print("2. Read files and folders")
print("3. Update the folder")
print("4. Delete the folder")

choice = int(input("Please enter your option: "))

if choice == 1:
    create_folder()
elif choice == 2:
    read_file_folder()
elif choice == 3:
    update_folder()
elif choice == 4:
    print("Choice 04")
else :
    print("Invalid Choice!!!\nPlease enter valid number!\nExample : 1")