"""19.2 (Testing full binary tree) A full binary tree is a binary tree
with the leaves on the same level. Add a method in the BST class to
return True if the tree is full. (Hint: The number of nodes in a full
binary tree is 2^depth -1.)

# Returns true if the tree is a full binary tree
def isFullBST():
"""
from Queue import Queue

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True

        return False

    # Insert element e into the binary search tree
    # Return Tue if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e:
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size

    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Displays the nodes in breadth-first traversal
    def breadthFirstTraversal(self):
        lst = []
        q = Queue()
        q.enqueue(self.root)

        while not q.isEmpty():
            a = q.dequeue()
            lst.append(a.element)
            if a.left != None:
                q.enqueue(a.left)
            if a.right != None:
                q.enqueue(a.right)

        for u in lst:
            print(u, end = " ")

    # Returns the height of this binary tree, i.e., the
    # number of the nodes in the longest path of the root to a leaf
    def height(self):
        return self.heightHelper(self.root)

    def heightHelper(self, node):
        if node == None:
            ret = 0

        else:
            ldepth = self.heightHelper(node.left) + 1
            rdepth = self.heightHelper(node.right) + 1

            ret = max(ldepth, rdepth)

        return ret

    def isFullBST(self):
        return self.isFullBSTHelper(self.root)

    def isFullBSTHelper(self, node):
##        print(node.element)
        if node == None:
##            print(1)
            ret = True
        elif node.left != None and node.right != None:
##            print(2)
##            a = self.isFullBSTHelper(node.left)
##            b = self.isFullBSTHelper(node.right)
            ret = self.isFullBSTHelper(node.left) and \
                  self.isFullBSTHelper(node.right)
##            ret = a and b
##            print(node.element)
##            print(ret)
        elif node.left == None and node.right == None:
##            print(3)
            ret = True
        else:
##            print(4)
            ret = False

        return ret

    # Returns a path from the root leading to the specified element
    def path(self, e):
        lst = []
        current = self.root # Start from here

        while current != None:
            lst.append(current) # Add the node on the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return lst # Return an array of nodes

    # Delete an element from the binary search tree
    # Return True if the element is deleted successfully
    # Return Flase if the element is not in the tree
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element:
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
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right

        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node iin the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightMost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

    

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None # Point to the left node, default None
        self.right = None # Point to the right node, default None


def main():
    tree = BST()
    tree.insert("George")
    tree.insert("Micheal")
    tree.insert("Tom")
    tree.insert("Adam")
##    tree.insert("Abraham")
    tree.insert("Jones")
    tree.insert("Peter")
##    tree.insert("Vik")
    tree.insert("Daniel")
    printTree(tree)
    print("Height of the tree is ", tree.height())

##    print("After delete George:")
##    tree.delete("George")
##    printTree(tree)
##
##    print("\nAfter delete Adam:")
##    tree.delete("Adam")
##    printTree(tree)
##
##    print("\nAfter delete Micheal:")
##    tree.delete("Micheal")
##    printTree(tree)
##
##    # Traverse tree
##    print("Inorder (sorted): ", end = "")
##    tree.inorder()
##    print("\nPostorder: ", end = "")
##    tree.postorder()
##    print("\nPreorder: ", end = "")
##    tree.preorder()
##    print("\nThe number of nodes is " + str(tree.getSize()))

    # Search for an element
    print("Is Peter in the tree? " + str(tree.search("Peter")))

    # Get a path from the root to Peter
    print("A path from the root to Peter is: ")
    path = tree.path("Peter")
    for node in path:
        print(node.element, end = " ")

    numbers = [2,4,3,1,8,5,6,7]
    intTree = BST()
    for e in numbers:
        intTree.insert(e)

    print("\nInorder (sorted): ", end = " ")
    intTree.inorder()
    print()
    print("The binary tree is full:", tree.isFullBST())

def printTree(tree):
    # Traverse tree
    print("Inorder (sorted): ", end = "")
    tree.inorder()
    print("\nPostorder: ", end = "")
    tree.postorder()
    print("\nPreorder: ", end = "")
    tree.preorder()
    print("\nBreadth First order: ", end = "")
    tree.breadthFirstTraversal()
    print("\nThe number of nodes is " + str(tree.getSize()))
    

if __name__ == "__main__":
    main()


        
        
    
                





















                
            
                
