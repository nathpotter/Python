import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Specify the directory path
path = Path(r'C:/Users/nath_/OneDrive/Documents/00_Jobs_Tutor/Python')
file_name = 'Date_CA.txt'
abs_file_path = os.path.join(path, file_name)

def read_file(file_name,TH_time,CA_time):
   
    if(os.path.exists(file_name) != True):
      with open(file_name, 'a') as fp:
        # uncomment below line if you want to create an empty file
       fp.write("\nConvert time from Thailand to Canada :")
       fp.write("\nInput:")
       THdate_time = TH_time.strftime("%m/%d/%Y, %H:%M:%S")
       CAdate_time = CA_time.strftime("%m/%d/%Y, %H:%M:%S")
       Line1=["\nTH_time:",THdate_time]
       fp.writelines(Line1) 
       Line2=["\nCA_time:",CAdate_time]
       fp.writelines(Line2)
       fp.close()

TH_dateTime = datetime.now(timezone(timedelta(hours=+7), 'MST'))
print("In TH::", TH_dateTime)


CA_dateTime = datetime.now(timezone(timedelta(hours=-7), 'MST'))
print("In CA::", CA_dateTime)

read_file(file_name,TH_dateTime,CA_dateTime)




