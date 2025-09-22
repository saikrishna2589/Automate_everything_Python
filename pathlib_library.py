#os and pathlib are used for
file_path = 'folder/123.txt'

with open('folder/abc.txt','r') as file:
    content = file.read()

print(content)
    #here notice using with open() method,file path is a string.

#lets use Path

from pathlib import Path
path_file_path = Path(file_path)
print(type(path_file_path))  #pathlib object


#if path doesnt exist, create file path and write content to the file
if not path_file_path.exists():
    with open(path_file_path,'w') as file:
        file.write('content123testfocusmodelovemywife')

#loop through files in folder
path_folder_path = 'folder'

folder_path = Path(path_folder_path) #pathlib object

print(folder_path.iterdir())  # generator object

dict_data={}

for sno, item in enumerate(folder_path.iterdir()):   #converts into iterator object
       with open(item, 'r') as file:
           content = file.read()  #read the data
           dict_data[sno] = content  #store it in the dict each reading

print(dict_data)


#extract filename with extension, filename and only extension
for item in folder_path.iterdir():
    name_of_files_with_extension = Path(item.name)  #filename with extension
    file_name_only = Path(item.stem)  #filename only without extension
    extension_only = Path(item.suffix) #extension type

print(name_of_files_with_extension)
print(file_name_only)
print(extension_only)


