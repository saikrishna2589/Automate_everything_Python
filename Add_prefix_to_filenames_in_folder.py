
from pathlib import Path #import pathlib

#access the folder iterate rename

folder_path =Path('folder')  #conver folder to pathlib using Path class

for item in folder_path.iterdir():
    new_file_name = "new" + "_" + item.stem + item.suffix
    #print(new_file_name)
    #item.replace(f"folder/{new_file_name}")

    new_file_path = item.with_name(new_file_name)
    print(new_file_path)
    item.rename(new_file_path)

    #creating filepath
    #with open(f'folder/{new_file_name}', 'w') as file:
        #file.write("")

    #if not new_file_name.exists():
      #  with open(f"folder/{new_file_name}",'w') as file:
          #  file.write()



#iterating through folder for list of files through iterdir() method of Pathlib
#then using rename method to