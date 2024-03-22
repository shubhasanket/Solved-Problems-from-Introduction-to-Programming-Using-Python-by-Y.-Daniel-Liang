'''22.3 (Implement DFS using a stack) The depth-first search algorithm
described in Listing 22.3 uses recursion. Implement it without using
recursion.
'''
from Queue import Queue
from Stack import Stack

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.neighbors = self.getAdjacnecyLists(edges)

    # Return a list of adjacency lists for edges
    def getAdjacnecyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(v) # Insert a neighbor for u
            
        return neighbors
    
    # Return the number of vertices in the graph
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index
    def getNeighbors(self, index):
        return self.neighbors[index]

    # Return the degree for a specified vertex
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print(self.getVertex(u) + " (" + str(u), end = "): ")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " +
                    str(self.neighbors[u][j]), end = ") ")
            print()
    
    # Clear graph
    def clear(self):
        vertices = []
        neighbors = []
    
    # Add a vertex to the graph
    def addVertex(self, vertex):
        if not (vertex in self.vertices):
            self.vertices.append(vertex)
            self.neighbors.append([]) # add a new empty adjacency list
    
    # Add an undirected edge to the graph
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            if not (indexV in self.neighbors[indexU]):
                self.neighbors[indexU].append(indexV)
    
    # Obtain a DFS tree starting from vertex v
    # To be discussed in Section 16.6
    def dfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1
        
        # Mark visited vertices
        isVisited = len(self.vertices) * [False]
        
        # Recursively search
        self.dfsHelper(v, parent, searchOrders, isVisited)
        # Return a search tree
        return Tree(v, parent, searchOrders, self.vertices)

    # Recursive method for DFS search
    def dfsHelper(self, v, parent, searchOrders, isVisited):
        # Store the visited vertex
        searchOrders.append(v)
        isVisited[v] = True # Vertex v visited
        
        for i in self.neighbors[v]:
            if not isVisited[i]:
                parent[i] = v # The parent of vertex i is v
                # Recursive search
                self.dfsHelper(i, parent, searchOrders, isVisited)

    # Obtain a DFS tree starting from vertex v
    # using a stack

    def dfs_stack(self, u):
        stack = Stack()
        parent_isVisited = len(self.vertices) * [-1, False]
        searchOrders = []
        stack.push((u,-1)) # (element, parent)
        searchOrders.append(u)
        parent_isVisited[u] = [-1, True]
        while not stack.isEmpty():
            j = stack.peek()
            for i in self.neighbors[j]:
                if parent_isVisited[i][1] == False:
                    stack.push((i,j))
                    
##        stack1 = Stack()
##        stack2 = Stack()
##        v = u
##        searchOrders = []
##        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1
##        # Mark visited vertices
##        isVisited = len(self.vertices) * [False]
####        isVisited[v] = True # Vertex v visited
##        stack1.push(v)
##        searchOrders.append(v)
##        isVisited[v] = True
####        for u in self.neighbours[v]:
####            stack2.push(u)
####        print("..")
##        while not stack1.isEmpty():
##            j = stack1.pop()
####            if isVisited[v] == False:
####                searchOrders.append(v)
##            for u in self.neighbors[j]:
##                stack2.push(u)
####            deleting = False
####            print("Loop1")
####            print(searchOrders)
####            print(stack1)
####            print(stack2)
##            while not stack2.isEmpty():
##                i = stack2.pop()
##                if isVisited[i] == False:
##                    isVisited[i] = True
##                    stack1.push(j)
##                    stack1.push(i)
##                    searchOrders.append(i)
##                    parent[i] = j
##                    stack2.delete()
####                print("Loop2")
####                    deteting = True
####           if not deleting:
##               
##        print(searchOrders)
##        print(parent)

        return Tree(u, parent, searchOrders, self.vertices)
                
                
                
    # Starting bfs search from vertex v
    # To be discussed in Section 16.7
    def bfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1
        
        queue = Queue() # the Queue class is defined in Chapter 12
        isVisited = len(self.vertices) * [False]
        queue.enqueue(v) # Enqueue v
        isVisited[v] = True # Mark it visited
        
        while not queue.isEmpty():
            u = queue.dequeue() # Dequeue to u
            searchOrders.append(u) # u searched
            for w in self.neighbors[u]:
                if not isVisited[w]:
                    queue.enqueue(w) # Enqueue w
                    parent[w] = u # The parent of w is u
                    isVisited[w] = True # Mark it visited
                    
        return Tree(v, parent, searchOrders, self.vertices)

# Tree class will be discussed in Section 16.5
class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root # The root of the tree
        # Store the parent of each vertex in a list
        self.parent = parent
        # Store the search order in a list
        self.searchOrders = searchOrders
        self.vertices = vertices # vertices of the graph

    # Return the root of the tree
    def getRoot(self):
        return self.root

    # Return the parent of vertex v
    def getParent(self, index):
        return self.parent[index]

    # Return an array representing search order
    def getSearchOrders(self):
        return self.searchOrders
    
    # Return number of vertices found
    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)
    
    # Return the path of vertices from a vertex index to the root
    def getPath(self, index):
        path = []
        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]
            
        return path
    
    # Print a path from the root to vertex v
    def printPath(self, index):
        path = self.getPath(index)
        print("A path from " + str(self.vertices[self.root]) + " to "
            + str(self.vertices[index]), end = ": ")
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end = " ")
            
    # Print the whole tree
    def printTree(self):
        print("Root is: " + str(self.vertices[self.root]))
        print("Edges: ", end = "")
        for i in range(len(self.parent)):
            if self.parent[i] != -1:
                # Display an edge
                print("(" + str(self.vertices[self.parent[i]])
                    + ", " + str(self.vertices[i]), end = ") ")
        
        print()

def main():
    edges = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3],
             [2, 4], [3, 1], [3, 2], [3, 4], [3, 5], [4, 2],
             [4, 3], [4, 5], [5, 3], [5, 4]]
##    edges = [[0,1], [0,2], [0,3], [1,0], [1,3], [2,0], [2,3],
##             [3,0], [3,1], [3,2], [4,5], [5,4]]

    vertices = [0,1,2,3,4,5]

    g = Graph(vertices, edges)
    t = g.dfs_stack(0)
    if t.getNumberOfVerticesFound() == len(vertices):
        print("The graph is connected")
    else:
        print("The graph is not connected")
    print(g.dfs(0).parent)
    print(g.dfs(0).searchOrders)
    

if __name__ == "__main__":
    main()














    
