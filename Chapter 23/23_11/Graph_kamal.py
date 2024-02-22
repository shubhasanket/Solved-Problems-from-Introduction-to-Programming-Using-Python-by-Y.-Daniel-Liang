#08/09/2020 Graph.py

#In this modification of the book's code, we have already added a method
#def getPath(self,u,v) which gets the path from u to v (Problem 22.05)
#this method can also be used for Problem 22.10 (shortest path)

#Now we will add two methods asked in Problems 22.06 and 22.07
#22.6 (Detect cycles) Add a new method in Graph to determine whether
#there is a cycle in the graph with the following header:
#def isCyclic():

#We have done the above using BFS (isCyclicBFS) and DFS (isCyclic)

#22.7 (Find a cycle) Add a new method in Graph to find a cycle in the graph
#with the following header:
#def getACycle()
#The method returns a list that contains all the vertices in a cycle
#from u to v in this order. If the graph has no cycles, the method returns None.
#It returns just one cycle.

# We also added another method: def getAllCycles() - print all cycles. But it is slow
# so do not use it for bigger sites with many cycles.
# Listing 22.2 Graph.py

from Queue import Queue
from Stack import Stack

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices  #List of vertices
        self.edges = edges        #Added - not in original
                                  #list of all edges - each edge is a list eg. [0,3]
        self.neighbors = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
        #print("Neighbors",neighbors,len(neighbors)  )  
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            #print("U",u,"V",v,"i",i)
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

    def isConnected(self):
        return (self.dfs(0).getNumberOfVerticesFound() == len(self.vertices))
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

    ####Problem 22.05
    def getPath(self, start, goal):  
        '''
        Finds a path from vertex u to vertex v and returns it as a
        list of integers.
        Returns None - if no path can be found
        This method  returns the shortest path (one of the shortes paths if
        there are more than one)
        '''

        if start == goal:
            return [start]

       
        queue = Queue()
        #We can use isVisited or searchOrders
        isVisited = len(self.vertices) * [False]           #####searchOrders = []

        queue.enqueue( [start] )# Enqueue start


        while not queue.isEmpty():
            #pop the first path from the queue
            p = queue.dequeue()
            #get the last node from the path
            vertex = p[-1]

            if not isVisited[vertex]:                      #####if vertex not in searchOrders: 
                neighbors = self.neighbors[vertex]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                print("Neighbors of vertex", vertex,neighbors)
                for n in neighbors:
                    
                    if isVisited[n]:     #####if n in searchOrders:  
                        continue
                    newPath = list(p)
                    newPath.append(n)
                    print("NewPath",newPath)
                    queue.enqueue(newPath)

                    # return path if neighbour is goal                  
                    if n == goal:
                        #yield p + [next]
                        return newPath
                #mark node as explored    
                
                isVisited[vertex] = True   #####searchOrders.append(vertex)
                print("Queue",queue)


        return None #no path


    ####Problem 22.06 Detect Cycles
    def isCyclicBFS(self):
        '''
        Returns True if there is a cycle in the graph - False otherwise.
        We can use either the DFS or the BFS method.
        We will use the BFS method as described by Jenny
        https://www.youtube.com/watch?v=vXrv3kruvwE
        '''
        
        searchOrders = []

        #vertexStatus takes three values
        #-1 we not looked at this vertex
        # 0 this vertex has gone into the queue
        #+1 this vertex has come out of the queue - we have examined it
        vertexStatus = len(self.vertices) * [-1] 
        
        queue = Queue() # 
        v = self.getIndex(self.vertices[0])
        queue.enqueue(v) # Enqueue v
        vertexStatus[v] = 0 #because v has got into the queue
        
        while not queue.isEmpty():
            u = queue.dequeue() # Dequeue to u
            n = self.getNeighbors(u)
            #Add all the neighbors into the queue
            for w in n:
                if vertexStatus[w] != 1:
                    if vertexStatus[w] == 0:
                        return True
                    queue.enqueue(w)
                    vertexStatus[w] = 0
            vertexStatus[u] = 1 #We have visited or explored u    

        return False

    ####Problem 22.06 Detect Cycles
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

##    def general_cyclic(self):
##        vertices = []
##        l = self.getConnectedComponents()
##        for u in l:
##            neighbors = []
##            for v in u:
##                i = self.getIndex(v)
##                neighbors.append(self.neighbors[i])
##            
##            g = Graph(u,[])
##            g.neighbors = 

    def getConnectedComponents(self):
        s = set(self.vertices)
        l = []
        while s:
            i = s.pop()
            t = self.dfs(i)
            s = s.difference(set(t.searchOrders))
            l.append(t.searchOrders)
            
        return l
    
    #22.7 (Find a cycle) Add a new method in Graph to find a cycle in the graph
    #with the following header:
    #def getACycle()
    #The method returns a list that contains all the vertices in a cycle
    #from u to v in this order. If the graph has no cycles, the method returns None.
    #Note it returns just one cycle.

    def getACycle(self):
        '''
        The method returns a list that contains all the vertices in a cycle
        from u to v in this order. If the graph has no cycles, the method returns None.
        It does not return all the cycles - just one cycle
        #https://stackoverflow.com/questions/12367801/finding-all-cycles-in-undirected-graphs#18388696
        '''
        if not self.isCyclic():
            return False
        
        #Graph has a cycle - self.edgeInCycle contains a list - one pair of vertices
        #in the cycle. Now we will try to find out the cycle on which this edge is present.

        self.found = False #This will become true when we find the cycle
        self.cycle = []    #This will contain the cycle when we find it

        path = [self.edgeInCycle[0]]  #To start path is a list containing one of the nodes
                                      #that is on the cycle
        self.findACycle(path)
        return self.cycle


    def findACycle(self,path):
        '''

        '''
        if self.found:  #We have found a cycle so return
            return
        start_node = path[0]
        next_node= None
        sub = []

        #visit each edge and each node of each edge
        k = len(self.edges)
        i = 0
        while i < k and not self.found:
        #for edge in graph:
            edge = self.edges[i]
            node1, node2 = edge
            if start_node in edge:
                    if node1 == start_node:
                        next_node = node2
                    else:
                        next_node = node1
                    if next_node not in path:
                            # neighbor node not on path yet
                            sub = [next_node]
                            sub.extend(path)
                            # explore extended path
                            self.findACycle(sub)
                    elif len(path) > 2  and next_node == path[-1]:
                            # cycle found
                            #print("***Cycle found",path)
                            p = self.rotate_to_smallest(path)
                            inv = self.invert(p)
                            self.cycle = inv[:] #path[:]  #.append(path)
                            self.found = True
                                
            i = i + 1                                


    def invert(self,path):
        return self.rotate_to_smallest(path[::-1])

    #  rotate cycle path such that it begins with the smallest node
    def rotate_to_smallest(self, path):
        n = path.index(min(path))
        return path[n:]+path[:n]

    def isNew(self, path,):
        return not path in self.cycles

    def visited(self, node, path):
        return node in path

    #22.7 Find a cycle 
    #Not asked in the problems - but we will try to write a function which will return
    #more than one cycle

    def getAllCycles(self):
        '''
        The method returns a list that contains all the cycles in a graph. Each cycle is
        an element in this list.
        If the graph has no cycles, the method returns None.
        #https://stackoverflow.com/questions/12367801/finding-all-cycles-in-undirected-graphs#18388696
        '''
        if not self.isCyclic():
            return False
        
        #Graph has a cycle 
        self.cycles = []    #This list contain all the cycles found - each cycle will be a list of vertices
        for edge in self.edges:
            for node in edge:
                self.findNewCycles([node])
        return self.cycles        


    def findNewCycles(self, path):
        start_node = path[0]
        next_node= None
        sub = []

        #visit each edge and each node of each edge
        for edge in self.edges:
            node1, node2 = edge
            if start_node in edge:
                    if node1 == start_node:
                        next_node = node2
                    else:
                        next_node = node1
                    if not self.visited(next_node, path):
                            # neighbor node not on path yet
                            sub = [next_node]
                            sub.extend(path)
                            # explore extended path
                            self.findNewCycles(sub);
                    elif len(path) > 2  and next_node == path[-1]:
                            # cycle found
                            p = self.rotate_to_smallest(path);
                            inv = self.invert(p)
                            if self.isNew(p) and self.isNew(inv):
                                self.cycles.append(p)
                                #print("Added",p)

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

