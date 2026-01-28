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

print("Options : ")

print("1. Create a folder")
print("2. Read files and folders")
print("3. Update the folder")
print("4. Delete the folder")

choice = int(input("Please enter your option: "))

if choice == 1:
    create_folder()
elif choice == 2:
    print("Choice 02")
elif choice == 3:
    print("Choice 03")
elif choice == 4:
    print("Choice 04")
else :
    print("Invalid Choice!!!\nPlease enter valid number!\nExample : 1")