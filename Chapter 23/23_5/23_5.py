'''23.5 (Prove or disprove) The conjecture is that both NineTailModel
and WeightedNineTailModel result in the same shortest path. Write a
program to prove or disprove it. (Hint: Let tree1 and tree2 denote the
trees rooted at node 511 obtained from NineTailModel and WeightedNineTailModel,
respectively. If the depth of a node u is the same in tree1 and
in tree2, the length of the path from u to the target is the same.)
'''
from WeightedNineTailModel import WeightedNineTailModel
from NineTailModel import getIndex
from NineTailModel import getNode
from NineTailModel import printNode
from NineTailModel import NineTailModel

def main():
    N = 511
    # Prompt the user to enter nine coins H's and T's
##    initialNode = \
##        input("Enter an initial nine coin H's and T's: ").strip()

    # Create the NineTaileModel
    model1 = WeightedNineTailModel()
##    path1 = model1.getShortestPath(getIndex(initialNode))
    tree1 = model1.tree

    model2 = NineTailModel()
##    path2 = model2.getShortestPath(getIndex(initialNode))
    tree2 = model2.tree

##    print("The steps to flip the coins are ")
##    for i in range(len(path)):
##        printNode(getNode(path[i]))  
##        
##    print("The number of flips is " + 
##        str(model.getNumberOfFlipsFrom(getIndex(initialNode))))
    p = True
    for i in range (N):
##        result = getNode(i) # we have the head/tails list representation of
                            # a node
        p1 = tree1.getPath(i)
        p2 = tree2.getPath(i)
##        print(p1)
##        print(p2)
##        print()
        if len(p1) != len(p2):
            p = False
            print('For the node', getNode(i),':')
            print('Path from WeightedNineTailModel is:',p1)
            print('Path from NineTailModel is:',p2)
            print('Thus the conjecture is FALSE')
            break

    if p:
        print('The conjecture is TRUE')
    
    
main()
