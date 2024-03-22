'''19.9 (Add new buttons in DisplayBST) Modify Listing 19.9, DisplayBST.py,
to add three new buttons Show Inorder, Show Preorder, and Show Postorder to
display the result in a message dialog box, as shown in Figure 19.21. You
need to add the following methods in the BST class to return a list of node
elements in inorder, preorder, and postorder:
def inorderList()
def preorderList()
def postorderList()
'''
from tkinter import *
import tkinter.messagebox
from BST import BST

def insert():
##    print(key)
    k = int(key.get())
    if tree.search(k): # key is in the tree
        tkinter.messagebox.showinfo("Insertion Status", str(k) +
                                    " is already in the tree")
    else:
        tree.insert(k)  # Insert a new key
        canvas.delete("tree")
        displayTree(tree.getRoot(), width/2, 30, width/4)

def delete():
    k = int(key.get())
    if not tree.search(k): # key is in the tree
        tkinter.messagebox.showinfo("Deletion Status", str(k) +
                                    " is not in the tree")
    else:
        tree.delete(k) # Delete a key
        canvas.delete("tree")
        displayTree(tree.getRoot(), width / 2, 30, width / 4)

def showPreorder():
    s = tree.preorderList()
    if s != None:
        tkinter.messagebox.showinfo("Preorder", str(s))
        
def showInorder():
    s = tree.preorderList()
    if s != None:
        tkinter.messagebox.showinfo("Inorder", str(s))

def showPostorder():
    s = tree.preorderList()
    if s != None:
        tkinter.messagebox.showinfo("Postorder", str(s))


# Display a subtree rooted at position (x, y)
def displayTree(root, x, y, hGap): 
    if root == None: return # Empty tree

    # Display the root
    canvas.create_oval(x - radius, y - radius,
                       x + radius, y + radius, tags = "tree")
    canvas.create_text(x, y,
                        text = str(root.element), tags = "tree")
    
    if root.left != None:
        # Draw a line to the left node
        connectTwoCircles(x - hGap, y + vGap, x, y)
        # Draw the left subtree recursively
        displayTree(root.left, x - hGap, y + vGap, hGap / 2)

    if root.right != None:
        # Draw a line to the right node
        connectTwoCircles(x + hGap, y + vGap, x, y)
        # Draw the right subtree recursively
        displayTree(root.right, x + hGap, y + vGap, hGap / 2)

# Connect two circles centered at (x1, y1) and (x2, y2)
def connectTwoCircles(x1, y1, x2, y2):
    d = (vGap * vGap + (x2 - x1) * (x2 - x1))**0.5
    x11 = x1 - radius * (x1 - x2) / d
    y11 = y1 - radius * (y1 - y2) / d
    x21 = x2 + radius * (x1 - x2) / d
    y21 = y2 + radius * (y1 - y2) / d
    canvas.create_line(x11, y11, x21, y21, tags = "tree")

##def main():
window = Tk() # Create a window 
window.title("DisplayBST") # Set a title

width = 500
height = 500
radius = 20
vGap = 50
canvas = Canvas(window, width = width, height = height)
canvas.pack()

frame1 = Frame(window) # Create and add a frame to window
frame1.pack()
tree = BST()
Label(frame1, text = "Enter a key").pack(side = LEFT)
key = StringVar()
entry = Entry(frame1, textvariable = key,
              justify = RIGHT).pack(side = LEFT)
Button(frame1, text = "Insert", command = insert).pack(side = LEFT)
Button(frame1, text = "Delete", command = delete).pack(side = LEFT)
Button(frame1, text = "Show Inorder", command = showInorder).pack(side = LEFT)
Button(frame1, text = "Show Preorder", command = showPreorder).pack(side = LEFT)
Button(frame1, text = "Show Postorder", command = showPostorder).pack(side = LEFT)

window.mainloop() # Create an event loop

##if __name__ == "__main__":
##    main()
    


    
        
