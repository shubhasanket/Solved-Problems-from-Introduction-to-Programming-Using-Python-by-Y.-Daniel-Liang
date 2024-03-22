'''20.4 (The kth smallest element) You can find the kth smallest
element in a BST in O(n) time from an inorder iterator. For an AVL
tree, you can find it in O(logn) time.
'''
import sys
from BST import BST
from BST import TreeNode

class AVLTree(BST):
    def __init__(self):
        BST.__init__(self)

    # Override the createNewNode method to create an AVLTreeNode
    def createNewNode(self, e):
        return AVLTreeNode(e)
    # Override the insert method to balance the tree if necessary
    def insert(self, o):
        successful = BST.insert(self, o)
        if not successful:
            return False # o is already in the tree
        else:
            self.balancePath(o) # Balance from o to the root if necessary
            self.updateSize()
            
        return True # o is inserted

    # Update the height of a specified node
    def updateHeight(self, node):
        if node.left == None and node.right == None: # node is a leaf
            node.height = 0
        elif node.left == None: # node has no left subtree
            node.height = 1 + (node.right).height
        elif node.right == None: # node has no right subtree
            node.height = 1 + (node.left).height
        else:
            node.height = 1 + max((node.right).height, (node.left).height)

    # Update the height of the entire tree 
    def updateSize(self):
        self.updateSizeHelper(self.root)
        
    # Update the height of a subtree starting at a specified node
    '''this method is working'''
    def updateSizeHelper(self, node):
        l = r = 0
        if node.left != None:
            self.updateSizeHelper(node.left)
            l = node.left.size
        if node.right != None:
            self.updateSizeHelper(node.right)
            r = node.right.size

        node.size = (r+l+1)
        

    # Balance the nodes in the path from the specified
    # node to the root if necessary
    def balancePath(self, o):
        path = BST.path(self, o)
        for i in range(len(path)-1, -1, -1):
            A = path[i]
            self.updateHeight(A)
            parentOfA = None if (A == self.root) else path[i-1]

            if self.balanceFactor(A) == -2:
                if self.balanceFactor(A.left) <= 0:
                    self.balanceLL(A, parentOfA) # Perform LL rotation
                else:
                    self.balanceLR(A, parentOfA) # Perform LR rotation

            elif self.balanceFactor(A) == 2:
                if self.balanceFactor(A.right) >= 0:
                    self.balanceRR(A, parentOfA) # Perform RR rotation
                else:
                    self.balanceRL(A, parentOfA) # Perform RL rotation

    # Return the balance factor of the node
    def balanceFactor(self, node):
        if node.right == None: # node has no right subtree
            return -node.height
        elif node.left == None: # node has no left subtree
            return +node.height
        else:
            return (node.right).height - (node.left).height

    # Balance LL
    def balanceLL(self, A, parentOfA):
        B = A.left # A is left-heavy and B is left-heavy

        if A == self.root:
            self.root = B
        else:
            if parentOfA.left == A:
                parentOfA.left = B
            else:
                parentOfA.right = B
        A.left = B.right # Make T2 the left subtree of A
        B.right = A # Make A the left child of B
        self.updateHeight(A)
        self.updateHeight(B)

    # Balance LR
    def balanceLR(self, A, parentOfA):
        B = A.left # A is left-heavy
        C = B.right # B is right-heavy
        if A == self.root:
            self.root = C
        else:
            if parentOfA.left == A:
                parentOfA.left = C
            else:
                parentOfA.right = C
        A.left = C.right # Make T3 the left subtree of A
        B.right = C.left # Make T2 the right subtree of B
        C.left = B
        C.right = A
        
        # Adjust heights
        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)

    
    # Balance RR
    def balanceRR(self, A, parentOfA):
        B = A.right # A is right-heavy and B is right-heavy

        if A == self.root:
            self.root = B
        else:    
            if parentOfA.left == A:
                parentOfA.left = B
            else:
                parentOfA.right = B

        A.right = B.left # Make T2 the right subtree of A
        B.left = A
        self.updateHeight(A)
        self.updateHeight(B)


    # Balance RL
    def balanceRL(self, A, parentOfA):
        B = A.right # A is right-heavy
        C = B.left # B is left-heavy
        
        if A == self.root:
            self.root = C
        else:
            if parentOfA.left == A:
                parentOfA.left = C
            else:
                parentOfA.right = C
                
        A.right = C.left # Make T2 the right subtree of A
        B.left = C.right # Make T3 the left subtree of B
        C.left = A
        C.right = B
        
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
            else: break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                root = current.right
            else:
                if element < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
            # Balance the tree if necessary
            self.balancePath(parent.element)
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
        self.updateSize()
        return True # Element inserted

    def find(self,k):
        if k < 1 or k > self.root.size:
            ret = None
        elif (self.root.left and self.root.right) == None:
            ret = None
        else:
            ret = self.findHelper(k,self.root)

        return ret

    def findHelper(self, k, node):
        A = node.left
        B = node.right

        if k == 0:
            return None
        elif k == 1 and A == None:
            return node.element
        elif k == 2 and A is None:
            return B.element
        elif k <= A.size:
            return self.findHelper(k,A)
        elif k == A.size + 1:
            return node.element
        else:
            return self.findHelper(k-A.size-1, B)
        

    
# AVLTreeNode is TreeNode plus height
class AVLTreeNode(TreeNode):
    def __init__(self, e):
        self.height = 0 # New data field
        self.size = 1
        TreeNode.__init__(self, e)
        


def main():
    tree = AVLTree()
    tree.insert(25)
    tree.insert(20)
    tree.insert(5)
    print("After inserting 25, 20, 5:")
    printTree(tree)
    
    tree.insert(34)
    tree.insert(50)
    print("After inserting 34, 50:")
    printTree(tree)
    tree.insert(30)
    print("After inserting 30")
    printTree(tree)

    for i in range(tree.size+2):
        print(tree.find(i))
##    l = tree.inorderListNode()
##    for u in l:
##        print(u.element, ": Size =", u.size)
    
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
    printTree(tree)


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
    



























    
