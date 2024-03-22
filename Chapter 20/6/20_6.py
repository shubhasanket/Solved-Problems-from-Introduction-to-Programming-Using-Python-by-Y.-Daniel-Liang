'''(Closest pair of points) Section 16.7 introduced an algorithm
for finding a closest pair of points in O(nlogn)time using a
divide-and-conquer approach. The algorithm was implemented
using recursion with a lot of overhead. Using the plain-sweep approach
along with an AVL tree, you can solve the same problem in O(nlogn)
time. Implement the algorithm using an AVLTree.
The sites used for this problem:
https://www.thealgorist.com/Algo/ClosestPair
https://www.thealgorist.com/Algo/SweepLine
https://www.thealgorist.com/Algo/RangeSearch
'''
import sys
sys.path.append(r'C:\Users\Shubham\AppData\Local\Programs\Python\Python39\Workspace\Chapter_20\20_6\mod')
import random
from AVLTree import AVLTree
from AVLTree import AVLTreeNode
from Div16_7Final import closest_pair
import time

##class AVLTreeUPD(AVLTreeNode):
##    def __init__(self):
##        AVLTreeNode.__init__(self)

class AVLTreeUPD(AVLTree):
    def __init__(self):
        AVLTree.__init__(self)

    def insert_multi(self,l):
        '''A list or a tuple is sent to this method
            and all its elements are inserted into the
            tree
        '''
        for u in l:
            self.insert(u)
##        print(self.inorderList())

##    def RangeQuery(self):
        
    
class CPOP:
    def __init__(self):
        N = 100000
        R = 1000000
        p = [(random.randrange(-R, R), random.randrange(-R, R)) \
             for i in range (N)]
        tree = AVLTreeUPD()
        tree.insert_multi(p)
        self.tree = tree
        proceed = True
        if (tree.root and tree.root.left) != None:
            self.d = self.distance(tree.root.element,tree.root.left.element)
            self.points = [tree.root.element, tree.root.left.element]
        elif (tree.root and tree.root.right) != None:
            self.d = self.distance(tree.root.element,tree.root.right.element)
            self.points = [tree.root.element, tree.root.right.element]

        else:
            proceed = False
        if proceed:
            t1 = time.time()
            self.inorder_traversal(tree.root)
            t2 = time.time()
##            self.points.sort()
            print("The closest pair of points is", self.points)
            print("Time taken is: ", round(t2-t1, 3))
            t1 = time.time()
            div_and_conq = closest_pair(p)
            t2 = time.time()
            print("The closest pair of points using the divide and conquer" +
                  " approach is", div_and_conq)
            print("Time taken is: ", round(t2-t1, 3))
        else:
            print("There is only 1 point")
##        print(p)
##        tree.insert_multi(p)
    def inorder_traversal(self, node):
        if node != None:
            self.inorder_traversal(node.left)
            self.RangeQuery(node)
            self.inorder_traversal(node.right)
        
    def RangeQuery(self, node):
        x_min_max = (node.element[0] - self.d, node.element[0]) # Contains the x threshold
        y_min_max = (node.element[1] - self.d, node.element[1] + self.d)
        # y_min_max contains the values of y - d and y + d
##        l = []
        lt = self.RangeQueryHelper(self.tree.root, x_min_max, y_min_max, [])
        for u in lt:
            #determine if a new minimum is found
            d = self.distance(node.element, u)
            if d < self.d and d != 0:
                self.d = d
                self.points = [u, node.element]

    def distance(self, node_xy, point_xy):
        # Calculates the distance between two points
        return ((node_xy[0]-point_xy[0])**2 + (node_xy[1]-point_xy[1])**2)**0.5

    def RangeQueryHelper(self, node, x_min_max, y_min_max, l):
        if node != None:
            if (x_min_max[0] <= node.element[0] <= x_min_max[1]):
                # If the current point is lying in the range
                # [x-d, x] where x is the x coordinate of the
                # point at which the sweep line is situated
                # then we enter into this routine
                if (y_min_max[0] <= node.element[1] <= y_min_max[1]):
                    # the current point also satisfies the condition on
                    # the y coordinate, thus we append it to the list
                    l.append(node.element)
                # we traverse its left and right node
                self.RangeQueryHelper(node.left, x_min_max, y_min_max, l)
                self.RangeQueryHelper(node.right, x_min_max, y_min_max, l)                
            elif node.element[0] < x_min_max[0]:
                # If the value of the node is less than the lower limit of
                # the range (say, the range is [lower, upper]), then traverse
                # only the right child node of the node because for all the
                # nodes in the left subtree, the x coordinates will be smaller
                # than 'lower'
                self.RangeQueryHelper(node.right, x_min_max, y_min_max, l)
            else:
                # If the value of the node is greater than the upper limit of
                # the range (say, the range is [lower, upper]), then traverse
                # only the left child node of the node because for all the
                # nodes in the right subtree, the x coordinates will be greater
                # than 'upper'
                self.RangeQueryHelper(node.left, x_min_max, y_min_max, l)

            return l
        
        
        
CPOP()


