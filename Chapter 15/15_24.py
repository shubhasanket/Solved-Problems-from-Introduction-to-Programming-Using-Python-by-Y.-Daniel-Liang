'''(Number of files in a directory) Write a program that prompts the
user to enter a directory and displays the number of files in the directory.
'''
import os
from tkinter.filedialog import askdirectory
import tkinter 
def main():
##    path = input("Enter a directory or a file: ").strip()
    tkinter.Tk().withdraw()
    path = askdirectory()
    try:
        print("There are", getNum(path), "files")
    except:
        print("The directory does not exist")

def getNum(path):
    num = 0
    
    if not os.path.isfile(path):
        lst = os.listdir(path)
        for subdirectory in lst:
            num += getNum(path + "/" +subdirectory)
    else:
        num += 1

    return num

main()
