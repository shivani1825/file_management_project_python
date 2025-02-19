import os
import shutil

def list_files():
    directory = input("Enter directory path: ")
    files = os.listdir(directory)
    if not files:
        print("No files found in the directory")
    else:  
        for file in files:
            print(file)

def rename_file():
    directory = input("Enter directory path: ")
    old_name = input("Enter old file name: ")
    new_name = input("Enter new file name: ")
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    print("File Renamed Successfully!")

def delete_path():
    directory = input("Enter directory path: ")
    name = input("Enter file or directory name to delete: ")
    path = os.path.join(directory, name)
    if os.path.isfile(path):
        os.remove(path)
        print("File deleted Successfully!")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print("Directory deleted successfully!")
    else:
        print("The Specified path does not exist.")

def create_directory():
    directory = input("Enter directory path: ")
    folder_name = input("Enter new folder name: ")
    path = os.path.join(directory, folder_name)
    os.makedirs(path, exist_ok=True)
    print("Directory created Successfully")

def move_file():
    source = input("Enter source file path: ")
    destination = input("Enter destination path: ")
    shutil.move(source, destination)
    print("File moved successfully!")

def copy_file():
    source = input("Enter source file path: ")
    destination = input("Enter destination path: ")
    shutil.copy(source, destination)
    print("File copied successfully!")

def get_file_size():
    file_path = input("Enter file path: ")
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        print(f"File size: {size} bytes")
    else:
        print("File does not exist.")

def main():
    menu_options = {
        "1": list_files,
        "2": rename_file,
        "3": delete_path,
        "4": create_directory,
        "5": move_file,
        "6": copy_file,
        "7": get_file_size,
        "8": exit
    }
    
    while True:
        print("\nFile Management System")
        print("1. List Files")
        print("2. Rename File")
        print("3. Delete File/Directory")
        print("4. Create Directory")
        print("5. Move File")
        print("6. Copy File")
        print("7. Get File Size")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        action = menu_options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

main()
