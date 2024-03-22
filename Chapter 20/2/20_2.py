'''(Comparing performance) Write a test program that randomly generates
500000 numbers and inserts them into a BST, reshuffles the 500000
numbers and performs search, and reshuffles the numbers again before
deleting them from the tree. Write another test program that does the
same thing for an AVLTree. Compare the execution times of these
two programs.
'''
import sys
import random
import time
sys.path.append(r'C:\Users\Shubham\AppData\Local\Programs\Python\Python39\Workspace\Chapter_20\20_2\mod')
from AVLTree import AVLTree
from BST import BST

def main(n):
    l = random.sample(range(0,10000000),n)
##    l = [i for i in range(n)]
    a = AVLTree()
    b = BST()
    at = time.time()
    for u in l:
        a.insert(u)
    at -= time.time()
    bt = time.time()
    for u in l:
        b.insert(u)
    bt -= time.time()
    print("Time taken to insert", n, "elements into a BST is", -bt)
    print("Time taken to insert", n, "elements into a AVLTree is", -at)
    print()

    random.shuffle(l)
    att = time.time()
    for u in l:
        a.search(u)
    att -= time.time()

    btt = time.time()
    for u in l:
        b.search(u)
    btt -= time.time()
    print("Time taken to search", n, "elements in a BST is", -btt)
    print("Time taken to search", n, "elements in a AVLTree is", -att)
    print()
    at += att
    bt += btt
    
    random.shuffle(l)
    att = time.time()
    for u in l:
        a.delete(u)
    att -= time.time()

    btt = time.time()
    for u in l:
        b.delete(u)
    btt -= time.time()
    print("Time taken to delete", n, "elements in a BST is", -btt)
    print("Time taken to delete", n, "elements in a AVLTree is", -att)
    print()
    at += att
    bt += btt
    print("Total time for the operations on the BST is", -bt)
    print("Total time for the operations on the AVLTree is", -at)

n = 500000
if __name__ == "__main__":
    main(n)
    
