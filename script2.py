import psutil
from sys import *


def ProcessDisplay():
    print("list of running processes ")

    Data=[]
    for proc in psutil.process_iter():
        value=proc.as_dict(attrs=['pid','name','username'])
        Data.append(value)
    return Data

def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : " + argv[0])


    arr=ProcessDisplay()

    for ele in arr:
        print(ele)


if __name__ == "__main__":
    main()
