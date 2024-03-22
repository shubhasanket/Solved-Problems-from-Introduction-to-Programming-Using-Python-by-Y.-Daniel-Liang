'''20.3 (Parent reference for BST) Suppose that the TreeNode class
defined in BST contains a reference to the node’s parent, as shown
in Exercise 7.20. Implement the AVLTree class to support this change.
Write a test program that adds numbers 1, 2, ..., 100 to the tree and
displays the paths for all leaf nodes.
'''
'''Making the necessary changes in the BST file contained in the folder
'''
import sys
import random
##print(sys.path)
##sys.path.append('C:\\Users\\Shubham\\AppData\\Local\\Programs\\Python\
##                \Python39\\Workspace\\Chapter_20\\20_3\\mod')
sys.path.append(r'C:\Users\Shubham\AppData\Local\Programs\Python\Python39\Workspace\Chapter_20\20_3\mod')
##print(sys.path)

from BST import TreeNode
from BST import BST
DEBUG = False
OUTSIDE = True

class AVLTree(BST):
    def __init__(self):
        BST.__init__(self)

    # Override the createNewNode method to create an AVLTreeNode
    def createNewNode(self, e, parent):
##        print(e, parent)
        return AVLTreeNode(e, parent)
    # Override the insert method to balance the tree if necessary
    def insert(self, o):
##        print(o)
        successful = BST.insert(self, o)
        if not successful:
            return False # o is already in the tree
        else:
            self.balancePath(o) # Balance from o to the root if necessary
            
        return True # o is inserted

    # Update the height of a specified node
    def updateHeight(self, node):
        if node.left == None and node.right == None: # node is a leaf
            node.height = 0
            if DEBUG:
                print("Case 1")
        elif node.left == None: # node has no left subtree
            node.height = 1 + (node.right).height
            if DEBUG:
                print("Case 2")
        elif node.right == None: # node has no right subtree
            node.height = 1 + (node.left).height
            if DEBUG:
                print("Case 3")
        else:
            node.height = 1 + max((node.right).height, (node.left).height)
            if DEBUG:
                print("Case 4")
        if DEBUG:
            pass
            
    # Balance the nodes in the path from the specified
    # node to the root if necessary
    def balancePath(self, o):
##        print("Balancing")
##        path = BST.path(self, o)
####        while 
##        for i in range(len(path)-1, -1, -1):
##            A = path[i]
##            self.updateHeight(A)
##            parentOfA = None if (A == self.root) else path[i-1]
##
##            if self.balanceFactor(A) == -2:
##                if self.balanceFactor(A.left) <= 0:
##                    self.balanceLL(A, parentOfA) # Perform LL rotation
##                else:
##                    self.balanceLR(A, parentOfA) # Perform LR rotation
##
##            elif self.balanceFactor(A) == 2:
##                if self.balanceFactor(A.right) >= 0:
##                    self.balanceRR(A, parentOfA) # Perform RR rotation
##                else:
##                    self.balanceRL(A, parentOfA) # Perform RL rotation

        node = self.det_node(o)
##        if DEBUG:
##            print(node.element)
##            print("Balance factor of node", node.element, "is",
##                  self.balanceFactor(node))
        while node != None:
            self.updateHeight(node)
            if DEBUG:
##                print(node.element)
                print("Balance factor of node", node.element, "is",
                      self.balanceFactor(node))
            if self.balanceFactor(node) == -2:
                if self.balanceFactor(node.left) <= 0:
                    self.balanceLL(node) # Perform LL rotation
                else:
                    self.balanceLR(node) # Perform LR rotation

            elif self.balanceFactor(node) == 2:
                if self.balanceFactor(node.right) >= 0:
                    self.balanceRR(node) # Perform RR rotation
                else:
                    self.balanceRL(node) # Perform RL rotation
            
            node = node.parent
        
    def det_node(self, e):
        current = self.root # Start from here
        parent = None
##        if DEBUG:
##            print("Root element is", self.root.element)
##            print("The element is", e)
##        if self.root.element == e:
##            ret = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
##                if DEBUG:
##                    print("|",current.element)
##                    print("|",parent.element)
            elif e > current.element:
                parent = current
                current = current.right
##                if DEBUG:
##                    print("|",current.element)
##                    print("|",parent.element)
            else:
##                if OUTSIDE:
##                    print("current:",current.element)
##                    print("parent:", parent.element)
##                    print(current.element == e)
                parent = current
                break
        
        if parent != None:
            if parent.element == e:
                ret = parent
            else:
                ret = None
        else:
            ret = None

        return ret
    # Return the balance factor of the node
    def balanceFactor(self, node):
        if node.right == None: # node has no right subtree
            return -node.height
        elif node.left == None: # node has no left subtree
            return +node.height
        else:
            if DEBUG:
                pass
            return (node.right).height - (node.left).height

    # Balance LL
    def balanceLL(self, A):
        if DEBUG:
            print('Performing LL')
        B = A.left # A is left-heavy and B is left-heavy

        if A == self.root:
            self.root = B
        else:
            if A.parent.left == A:
                A.parent.left = B
            else:
                A.parent.right = B
        B.parent = A.parent # As B replaces A
        A.left = B.right # Make T2 the left subtree of A
        if A.left != None:
            A.left.parent = A
        B.right = A # Make A the right child of B
        if B.right != None:
            B.right.parent = B

        # Adjust heights
        self.updateHeight(A)
        self.updateHeight(B)

    # Balance LR
    def balanceLR(self, A):
        if DEBUG:
            print('Performing LR')
        B = A.left # A is left-heavy
        C = B.right # B is right-heavy
        if A == self.root:
            self.root = C
        else:
            if A.parent.left == A:
                A.parent.left = C
            else:
                A.parent.right = C
        C.parent = A.parent
        A.left = C.right # Make T3 the left subtree of A
        if A.left != None:
            A.left.parent = A
        B.right = C.left # Make T2 the right subtree of B
        if B.right != None:
            B.right.parent = B
        C.left = B
        if C.left != None:
            C.left.parent = C
        C.right = A
        if C.right != None:
            C.right.parent = C
        
        # Adjust heights
        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)

    
    # Balance RR
    def balanceRR(self, A):
        if DEBUG:
            print('Performing RR')
        B = A.right # A is right-heavy and B is right-heavy

        if A == self.root:
            self.root = B
        else:    
            if A.parent.left == A:
                A.parent.left = B
            else:
                A.parent.right = B
        B.parent = A.parent
        A.right = B.left # Make T2 the right subtree of A
        if A.right != None:
            A.right.parent = A
        B.left = A
        if B.left != None:
            B.left.parent = B
        
        # Adjust heights
        self.updateHeight(A)
        self.updateHeight(B)


    # Balance RL
    def balanceRL(self, A):
        if DEBUG:
            print('Performing RL')
        B = A.right # A is right-heavy
        C = B.left # B is left-heavy
        
        if A == self.root:
            self.root = C
        else:
            if A.parent.left == A:
                A.parent.left = C
            else:
                A.parent.right = C

        C.parent = A.parent       
        A.right = C.left # Make T2 the right subtree of A
        if A.right != None:
            A.right.parent = A
        B.left = C.right # Make T3 the left subtree of B
        if B.left != None:
            B.left.parent = B
        C.left = A
        if C.left != None:
            C.left.parent = C
        C.right = B
        if C.right != None:
            C.right.parent = C
        
        # Adjust heights
        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)

    # Delete an element from the binary tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree
    def delete(self, element):
        if self.root == None:
            return False # Element is not in the tree
        # Locate the node to be deleted and also locate its parent node
        parent = None
        current = self.root
        while current != None:
            if element < current.element:
                parent = current
                current = current.left
            elif element > current.element:
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree
                
        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
                if current.right != None:
                    self.root.parent = None
            else:
                if element < parent.element:
                    parent.left = current.right
                    if parent.left != None:
                        parent.left.parent = parent
                else:
                    parent.right = current.right
##                    parent.left.parent = parent
                    if parent.left != None:
                        parent.left.parent = parent
            # Balance the tree if necessary
##            self.balancePath(parent.element)
            try:
                self.balancePath(parent.element)
            except:
                pass
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
            # Special case: parentOfRightMost is current
                parentOfRightMost.left = rightMost.left

            # Balance the tree if necessary
            self.balancePath(parentOfRightMost.element)

        self.size -= 1 # One element deleted
        return True # Element inserted

    
# AVLTreeNode is TreeNode plus height
class AVLTreeNode(TreeNode):
    def __init__(self, e, parent = None):
        self.height = 0 # New data field
##        print(".",e,parent)
        TreeNode.__init__(self, e, parent)

def main():
    tree = AVLTree()
    n = 100
##    l = [i for i in range (40)]
##    temp = []+l
##    random.shuffle(l)
##    print(l)
##    l = [19, 17, 38, 21, 23, 14, 29, 18, 10, 20, 15, 31, 6,
##         7, 28, 9, 26, 24, 30, 0, 1, 27, 11, 3, 12, 34, 5, 37,
##         13, 22, 36, 35, 32, 16, 4, 39, 33, 25, 2, 8]
##    temp = []+l
##    for u in l:
##        tree.insert(u)
##    for u in temp:
##        path = tree.path(u)
##        print(str(u)+":", end = " ")
##        for i in path:
##            print(str(i.element)+", ", end = "")
##        print()
##    for i in range (1,20):
##        tree.delete(i)
##    for i in range (1,20):
##        tree.insert(i)
##    printTree(tree)
            
    for i in range (1,n+1):
##        print('Inserting', i)
        tree.insert(i)
##        print('The root is',tree.root.element)
##    printTree(tree)
    l = tree.inorderNodeList()
    a = []
    for i in l:
        if (i.right and i.left) == None:
            a.append(i)
        
    for i in a:
##        if (i.right and i.left) == None:
        path = tree.path(i.element)
        path.pop()
##        print(path)
        print(str(i.element)+":", end = " ")
        for u in path:
            print(str(u.element)+", ", end = "")
        print()
    print("--------------------------------")
##    node = tree.det_node(0)
####    print(node.element)
##    while node != None:
##        print(node.element)
##        node = node.parent
    
##    tree.insert(25)
##    tree.insert(20)
##    tree.insert(5)
##    print("After inserting 25, 20, 5:")
##    printTree(tree)
##    
##    tree.insert(34)
##    tree.insert(50)
##    print("After inserting 34, 50:")
##    printTree(tree)
##    tree.insert(30)
##    print("After inserting 30")
##    printTree(tree)
##    
##    tree.insert(10)
##    print("After inserting 10")
##    printTree(tree)
##    
##    tree.delete(34)
##    tree.delete(30)
##    tree.delete(50)
##    print("After removing 34, 30, 50:")
##    printTree(tree)
##    
##    tree.delete(5)
##    print("After removing 5:")
##    printTree(tree)
##    tree.delete(20)
##    print("After deleting 20")
##    printTree(tree)
##    tree.insert(25)
##    tree.insert(20)
##    tree.insert(5)
##    print("After inserting 25, 20, 5:")
##    printTree(tree)
##    
##    tree.insert(34)
##    tree.insert(50)
##    print("After inserting 34, 50:")
##    printTree(tree)
##    tree.insert(30)
##    print("After inserting 30")
##    printTree(tree)
##    tree.delete(10)
##    print("After deleting 10")
##    printTree(tree)
##    tree.delete(25)
##    print("After deleting 25")
##    printTree(tree)
##    tree.delete(5)
##    tree.delete(50)
##    tree.delete(30)
##    tree.delete(20)
##    tree.delete(34)
##    printTree(tree)

def printTree(tree):
    # Traverse tree
    print("Inorder (sorted): ", end = "")
    tree.inorder()
    print("\nPostorder: ", end = "")
    tree.postorder()
    print("\nPreorder: ", end = "")
    tree.preorder()
    print("\nThe number of nodes is " + str(tree.getSize()))
    print()

if __name__ == "__main__":
    main()
    



























    
