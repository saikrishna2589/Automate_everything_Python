from pathlib import Path

folder_path =  Path('folder')

print(folder_path.glob('**'))

for item in folder_path.glob('**/*'):
    if item.is_file():  #access the text files
        item_parts_tuple= item.parts   #prints parts of the file path of the pathlib object
        #access only the sub-folder name from the tuple indexing 2nd element
        sub_folder_name =item_parts_tuple[1]
        # construct the string name of the new file name we wanted
        new_file_name = sub_folder_name + '_' + item.name
        #now building the file path
        new_file_path = item.with_name(new_file_name)
        print(new_file_path)
        #rename the filepath with new file path
        item.rename(new_file_path)





