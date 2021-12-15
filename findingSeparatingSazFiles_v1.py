# Import the module
import csv, json
import os 
import  tkinter as tk
import shutil
import pandas as pd
from tkinter import filedialog


root = tk.Tk()
root.withdraw()


current_path = os.getcwd()
file_path = filedialog.askopenfilename(initialdir=current_path)
print("\nPlease wait............... ")

splitted_path = file_path.split("\\")
csv_checker = splitted_path[-1]
if 'csv' in csv_checker:
    df = pd.read_csv(file_path)
    pid_saved_column = list(df['_Product_id'].values)

    ## Get overall Files in the folder
    saz_files = os.listdir()


    if 'text' in pid_saved_column:
        pid_saved_column.remove('text')


    MYDIR = ("Deliverable_BU_Files")
    CHECK_FOLDER = os.path.isdir(MYDIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)


    counter = 0
    present_saz = []
    for saz in saz_files:
        if '.saz' in saz:
            split = saz.split(".saz")
            present_saz.append(split[0])
            file_name = split[0]+".saz"
            if (split[0] in pid_saved_column) and (file_name not in os.listdir(current_path+"\\"+MYDIR)):
                counter += 1
                shutil.copyfile(current_path+"\\"+file_name, current_path+"\\"+MYDIR+"\\"+file_name)

    missing_saz = []
    for missing in pid_saved_column:
        if missing not in present_saz:
            missing_saz.append(missing)

    print("\n^^^^^^^^^^^^^ Files are successfully copied to Folder: "+MYDIR+" ^^^^^^^^^^^^^")

    if len(missing_saz) > 0:
        print("\n************ Missing Files Product_IDs ************")
        print(missing_saz)
    else:
        print("\n************ Congratulations No missing Files ************\n")

else:
    print("\n !!!!!!!!!!!!!!!!! Error: Wrong File Selected, Hint: It is not a CSV file !!!!!!!!!!!!!!!!!")

