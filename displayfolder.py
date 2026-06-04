import os
def show_folder(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print("Folder:", item)
            show_folder(full_path)
        else:
            print("File:", item)
folder_path = input("Enter folder path: ")
show_folder(folder_path)
