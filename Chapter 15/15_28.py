'''(Find words) Write a program that finds all the occurrences
of a word in all the files under a directory, recursively. Your
program should prompt the user to enter a directory name.
'''
import os
from tkinter.filedialog import askdirectory
import tkinter 
def main():
##    path = input("Enter a directory or a file: ").strip()
##    word = input("Enter the word you want to look for in the directory: ").strip()
    w = tkinter.Tk()#.withdraw()
##    w.withdraw()
    path = askdirectory()
    w.update()
##    word = input("Enter the word you want to look for in the directory: ").strip()
##    print("hello")
    try:
        print("The word "+word+" occurs", getNum(path), "times")
    except:
        print("There exists a file in the directory that cannot be read")

def getNum(path):
    num = 0
    
    if not os.path.isfile(path):
        lst = os.listdir(path)
        for subdirectory in lst:
            num += getNum(path + "/" +subdirectory)
    else:
        inf = open(path,"r")
        l = inf.readlines()
        inf.close()
        for u in l:
            v = u.split()
            for w in v:
                if w.strip() == word:
                    num += 1
    return num

word = input("Enter the word you want to look for in the directory: ").strip()
main()
