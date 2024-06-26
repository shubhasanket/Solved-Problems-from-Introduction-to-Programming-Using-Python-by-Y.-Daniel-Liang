# Listing 22.2 Graph.py

from Queue import Queue

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

    def isCyclic(self,vertice):
        '''
        Returns True if there is a cycle in the graph - False otherwise.
        We can use either the DFS or the BFS method. This uses the DFS method.
        '''

        parent = self.getSize() * [-1] # Initialize parent[i] to -1
        searchOrder = []
        s = Stack()
        s.push(self.getIndex(vertice))
        while not s.isEmpty():
            p = s.pop()
            if p not in searchOrder:
                searchOrder.append(p)
                n = self.neighbors[p]
                
                for i in n:
                    if i not in searchOrder:
                        s.push(i)
                        parent[i] = p
            else:
                father = parent[p]
                k = searchOrder.index(father)
                self.edgeInCycle = searchOrder[k:]
                return True      
            
        return False


    def getAllHamiltonianCycles(self): # Using backtracking
        al = []
        for u in range (len(self.vertices)):
            l = [] # list containing the order of the Hamiltonian
                    # cycle
    ##        vertice_0 = vertices[0]
            l.append(u)
            mem = [-1]*(len(self.vertices)-1)
            r = 0

            while r!= -1:
                v = l[r] # index of the current vertice we are looking at
                i = mem[r] # the index of the next vertice in l
                if i == (len(self.neighbors[v])-1):
                    # there are no other vertices left in the neighbors
                    # list of v that can be appended
                    mem[r] = -1
                    r -= 1
                    l.pop()
                    #continue
                else:
                    # when we have not exhausted all possibilities
                    found_new_vertice = False
                    for u in range (i+1, len(self.neighbors[v])):
                        if self.neighbors[v][u] not in l:
                            l.append(self.neighbors[v][u])
                            mem[r] = u
                            r += 1
                            found_new_vertice = True
                            break
                    if not found_new_vertice:
                        mem[r] = -1
                        r -= 1
                        l.pop()
                if len(l) == len(self.vertices):
##                    print(l)
                    # this means l is complete
                    # check whether 0 is in the neighbors list of
                    # the last element in the list
                    if l[0] in self.neighbors[l[-1]]:
##                        print(l)
                        # we have a hamiltonian cycle
                        al.append([]+l)
##                        print(al)

                    r -= 1
                    l.pop()
##                    else: # we do not have a hamiltonian cycle
##                        r -= 1
##                        l.pop()

        if al:# if al is not empty
            return al
        else:
            # When the graph has no hamiltonian cycle
            return None

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
