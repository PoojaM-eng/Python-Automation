import os
import time
import psutil
from sys import *


def ProcessDisplay(FolderName="Marvellous"):


    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    else:
        print("destination directory is already present")

    Data = []
    File_Path = os.path.join(FolderName, "Marvellous.log")
    fd = open(File_Path, "w")

    for proc in psutil.process_iter():
        value = proc.as_dict(attrs=['pid', 'name', 'username'])
        Data.append(value)

    for element in Data:
        fd.write("%s\n" % element)

def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : " + argv[0])

    if (len(argv)!=2):
        print("insufficient arguments")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name_directory_name")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help: it is use to create log file of running processes")
        exit()
    ProcessDisplay(argv[1])



if __name__ == "__main__":
    main()
