#add datetime details on when the files in the test folders were created.

from pathlib import Path
from datetime import datetime

path_folder_path =Path('folder')


for item in path_folder_path.glob('**/*'):
    if item.is_file():
        print(item)  #file path
        #construct string object of the file name
        #first get the date of file created.

        # this will give file size,user who created,date modified,created etc.
        stats_of_file = item.stat()
        file_unix_date_created = stats_of_file.st_ctime

        #convert the file_date_created in seconds unix(since 1970 till date) into datetime human readable.

        file_datetime = datetime.fromtimestamp(file_unix_date_created)  #.fromtimestamp unix to datetime
        print(type(file_datetime))  #this will be datetime class

        #convert to string so we can use the datetime string type in filename
        string_datetime = file_datetime.strftime("%Y-%m-%d_%H-%M-%S")

        #construct new file name
        file_path_parts = item.parts

        sub_folder_name= file_path_parts[1]

        new_file_name = f"{string_datetime}_{sub_folder_name}_{item.name}"

        #construct file path
        new_file_path = item.with_name(new_file_name)
        print(new_file_path)
        #rename current file path with new file path
        item.rename(new_file_path)







