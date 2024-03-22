'''(Tkinter: Count the occurrences of each letter) Rewrite Listing 14.5 using a GUI
program to let the user enter the file from an entry field, as shown in Figure 14.3a.
You can also select a file by clicking the Browse button to display an Open file dialog
box, as shown in Figure 14.3b. The file selected is then displayed in the entry
field. Clicking the Show Result button displays the result in a text widget. You
need to display a message in a message box if the file does not exist.
'''
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os

class GUI_occurences:
    def __init__(self):
        window = Tk()
        window.title("Occurences of Letters")
        
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1)
        
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)

        self.text = Text(frame1, width = 40, height = 20, wrap = WORD,
                         yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)

        frame2 = Frame(window)
        frame2.grid(row = 2, column = 1)

        label = Label(frame2, text = "Enter a filename:")
        label.grid(row = 1, column = 1, sticky = W)
        
        self.path = StringVar()
        self.entry = Entry(frame2, textvariable = self.path, justify = LEFT)
        self.entry.grid(row = 1, column = 2, sticky = W)

        buttonB = Button(frame2, text = "Browse", command = self.browse)
        buttonB.grid(row = 1, column = 3, sticky = W)

        buttonS = Button(frame2, text = "Show Result", command = self.show)
        buttonS.grid(row = 1, column = 4)

##        window.update()
##        self.path.set(askopenfilename())
##        self.entry.focus_set()
        window.bind("<Return>", self.process_event)
        window.bind("<b>", self.process_event)
        window.focus_set()
        window.mainloop()
        
    def browse(self):
        self.path.set(askopenfilename())

    def show(self):
        path_ = self.path.get()
        if not os.path.isfile(path_):
            tkinter.messagebox.showerror("Error", "Path is incorrect")

        else:
            self.text.delete("1.0", "end")
            inf = open(self.path.get(), 'r')
            d = {}
            a = inf.readline()
            while a != '':
                for i in a:
                    if i.isalpha():
                        if i in d:
                            d[i] += 1
                        else:
                            d[i] = 1
                a = inf.readline()
            inf.close()
            
            s = ''
            a = ord('a')
            for i in range (26):
                if chr(a+i) in d:
                    j = d[chr(a+i)]
                else:
                    j = 0
                s += chr(a+i) + " appears " +str(j) + " times\n"
##                print(chr(a+i) + " appears", j, "times")
                
            self.text.insert(1.0, s)    

    def process_event(self, event):
        if event.keysym == "Return":
            self.show()
        else:
            self.browse()

GUI_occurences()
