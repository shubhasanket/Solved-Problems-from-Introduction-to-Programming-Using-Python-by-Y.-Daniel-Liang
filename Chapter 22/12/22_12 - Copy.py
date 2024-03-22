'''22.12 (4 × 4 16 tail model) The nine tail problem in the text uses
a 3 × 3 matrix. Assume that you have 16 coins placed in a 4 × 4 matrix.
Create a new model class named TailModel22.
Create an instance of the model and save the object into a file named
Exercise22_12.dat.
'''

from Graph import Graph
from Graph import Tree
import pickle

N = 4
N2 = N**2
NUMBER_OF_NODES = 2**N2

class NineTailModel:
    def __init__(self):
        edges = self.getEdges()
        
        # Create a graph
        vertices = [x for x in range(NUMBER_OF_NODES)]
        graph = Graph(vertices, edges)

        # Obtain a BSF tree rooted at the target node
        self.tree = graph.bfs(NUMBER_OF_NODES-1)
        name = str(N)+"_"+".dat"
        outfile = open(name, "wb")
        pickle.dump(self, outfile)
        outfile.close()

    def getShortestPath(self, nodeIndex):
        return self.tree.getPath(nodeIndex)
    
    def printNode(self, node):
        for i in range(N2):
            if i % N != (N-1):
                print(node[i], end = " ")
            else:
                print(node[i])

        print()

    # Create all edges for the graph 
    def getEdges(self):
        edges = [] # Store edges
        for u in range(NUMBER_OF_NODES):
            for k in range(N2):
                node = self.getNode(u) # Get the node for vertex u
                if node[k] == 'H':
                    v = self.getFlippedNode(node, k)
                    # Add edge (v, u) for a legal move from node u to node v
                    edges.append([v, u])
                    
        return edges

    def getFlippedNode(self, node, position):
        row = position // N
        column = position % N

        self.flipACell(node, row, column)
        self.flipACell(node, row - 1, column)
        self.flipACell(node, row + 1, column)
        self.flipACell(node, row, column - 1)
        self.flipACell(node, row, column + 1)
        # Adding the following lines for problem 22.11
    ##    flipACell(node, row - 1, column - 1)
    ##    flipACell(node, row - 1, column + 1)
    ##    flipACell(node, row + 1, column - 1)
    ##    flipACell(node, row + 1, column + 1)
        

        return self.getIndex(node)

    def getIndex(self,node):
        result = 0

        for i in range(N2):
            if node[i] == 'T':
                result = result * 2 + 1
            else:
                result = result * 2 + 0

        return result
        
    def flipACell(self, node, row, column):
        if row >= 0 and row <= (N-1) and column >= 0 and column <= (N-1): 
            # Within the boundary
            if node[row * N + column] == 'H':
                node[row * N + column] = 'T' # Flip from H to T
            else:
                node[row * N + column] = 'H' # Flip from T to H
    ##    else:
    ##        print(row, column)
     
    def getNode(self, index):
        result = N2 * [' ']

        for i in range(N2):
            digit = index % 2
            if digit == 0:
                result[(N2-1) - i] = 'H'
            else:
                result[(N2-1) - i] = 'T'
            index = index // 2

        return result

def main():
##    NineTailModel()
    initialNode = input("Enter an initial nine coin H's and T's: ").strip()
    file = open(str(N)+"_"+".dat", "rb")
    model = pickle.load(file)
    file.close()
##    print(model)
##    model = NineTailModel()
    path = model.getShortestPath(model.getIndex(initialNode))

    print("The steps to flip the coins are ");
    for i in range(len(path)):
        model.printNode(model.getNode(path[i]))

if __name__ == "__main__":
    main()

















    
