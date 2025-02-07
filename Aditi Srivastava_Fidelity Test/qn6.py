import os
def count_files_folders(drive_path):
    file_count = 0
    folder_count = 0

    for dirs,files in os.walk(drive_path):
        folder_count += len(dirs)
        file_count += len(files) 

    print("Drive: {drive_path}")
    print("Total Folders: {folder_count}")
    print("Total Files: {file_count}")
drive = "C:\DBMS"
count_files_folders(drive)
