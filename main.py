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

def delete_folder():
    try:
        read_file_folder()
        name = input("Please tell which folder you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            p.rmdir()
            print("Your folder was deleted successfully! ✅")
        else:
            print("No such folder exist!")    
    except Exception as err:
        print(f"Sorry an error occured as {err}")
        
def create_file():
    try:
        read_file_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Write what you want in this file: ")
                fs.write(data)
            print("Your file was created successfully! ✅")
        else :
            print("Sorry this file name already exist!")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

    
def read_file():
    print("Read File")

def update_file():
    print("Update File")
    
def delete_file():
    print("Delete File")

print("Options : ")

print("1. Create a folder")
print("2. Read files and folders")
print("3. Update the folder")
print("4. Delete the folder")
print("5. Create a File")
print("6. Read a File")
print("7. Update a File")
print("8. Delete a File")

choice = int(input("Please enter your option: "))

if choice == 1:
    create_folder()
elif choice == 2:
    read_file_folder()
elif choice == 3:
    update_folder()
elif choice == 4:
    delete_folder()
elif choice == 5:
    create_file()
elif choice == 6:
    read_file()
elif choice == 7:
    update_file()
elif choice == 8:
    delete_file()
else :
    print("Invalid Choice!!!\nPlease enter valid number!\nExample : 1")