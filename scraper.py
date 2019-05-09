#%%
import os
import shutil

SOURCE_DIRECTORY = os.path.join("C:\\", "Users", "Max", "Documents", "Junk", "test1")
DEST_DIRECTORY = os.path.join("C:\\", "Users", "Max", "Documents", "Junk", "test2")

#%%
def list_folders(directory):
    file_list = os.listdir(directory)
    folders = []
    for file in file_list:
        if os.path.isdir(os.path.join(directory, file)):
            folders.append(file)
    return(folders)
    
def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)
#%%
src_folders = list_folders(SOURCE_DIRECTORY)
dst_folders = list_folders(DEST_DIRECTORY)

missing_folders = [folder for folder in src_folders if (not(folder in dst_folders))]

if (len(missing_folders) == 0):
    print("Rowley is already up to date.")
else:
    print("Found {} folders to copy to Rowley.".format(len(missing_folders)))
    
#%%
for folder_to_copy in missing_folders:
    copytree(src = os.path.join(SOURCE_DIRECTORY, folder_to_copy),
             dst = os.path.join(DEST_DIRECTORY, folder_to_copy))
    print("Copied {} to Rowley.".format(folder_to_copy))