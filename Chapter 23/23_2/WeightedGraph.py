'''23.2 (Implementing Prim’s algorithm using adjacency matrix) The text
implements Prim’s algorithm using priority queues on adjacent edges.
Implement the algorithm using adjacency matrix for weighted graphs.
'''

from Graph_kamal import Graph
from Graph import Tree
from WeightedEdge import WeightedEdge
from Heap import Heap # Heap is covered in Chapter 11
from copy import deepcopy

MAX_VALUE = 1e+308 # Infinity
DEBUG = not True
DEBUG1 = not True
DEBUG3 = not True
class WeightedGraph(Graph):
    def __init__(self, vertices, edges):
        self.vertices = vertices
        Graph.__init__(self, vertices, getEdges(edges))
        self.queues = self.getQueueForWeightedEdge(edges)
        self.matrix = gen_matrix(edges)
##        print(self.matrix)
##        self.check_queues()
        
##    def check_queues(self):
##        queues = deepcopy(self.queues)
##        for i in queues:
##            while not i.isEmpty():
##                a = i.remove()
##                print([a.u,a.v,a.weight])
             
    def getQueueForWeightedEdge(self, edges):
        queues = []
        for i in range(len(self.getVertices())):
            # Each element in the queue is a heap
            queues.append(Heap()) 
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            weight = edges[i][2]
            # Insert an edge into the heap
            queues[u].add(WeightedEdge(u, v, weight)) 

        return queues
    
    #Display edges with weights 
    def printWeightedEdges(self):
        for i in range(len(self.queues)):
            print(str(self.getVertex(i)) 
                  + " (" + str(i), end = "): ")
            for edge in self.queues[i].getLst():
                print("(" + str(edge.u) + ", " + str(edge.v) 
                      + ", "  + str(edge.weight), end = ") ")
            print()

    # Get the edges from the weighted graph 
    def getWeightedEdges(self):
        return self.queues
  
    # Clears the weighted graph 
    def clear(self):
        Graph.vertices.clear()
        Graph.neighbors.clear()
        self.queues.clear()
  
    # Add vertices to the weighted graph 
    def addVertex(vertex):
        Graph.addVertex(vertex)
        queues.add(Heap())

    # Add edges to the weighted graph 
    def addEdge(u, v, weight):
        Graph.addEdge(u, v);
        queues[u].add(WeightedEdge(u, v, weight))

    # Get a minimum spanning tree rooted at vertex 0 */
    def getMinimumSpanningTree(self):
        return self.getMinimumSpanningTreeAt(0)
    
    # Get a minimum spanning tree rooted at a specified vertex 
    def getMinimumSpanningTreeAt(self, startingIndex):
        # T initially contains the startingVertex;
        T = [startingIndex]
    
        numberOfVertices = len(self.vertices) # Number of vertices
        # Initially set the parent of all vertices to -1
        parent = numberOfVertices * [-1] # Parent of a vertex
    
        totalWeight = 0 # Total weight of the tree thus far
    
        # Clone the queues, so to keep the original queue intact
        queues = deepClone(self.queues)
    
        # All vertices are found?
        while len(T) < numberOfVertices:
            # Search for the vertex with the smallest edge 
            # adjacent to a vertex in T
            v = -1
            smallestWeight = MAX_VALUE
            queues = deepClone(self.queues)
            for u in T:
##                while not queues[u].isEmpty():
##                    a = queues[u].remove()
##                    print(a.u, a.v, a.weight)
##                queues = deepClone(self.queues)
                while not queues[u].isEmpty() and \
                    queues[u].peek().v in T:
                    if DEBUG1:
                        print('T =',T)
                        print('u =',u)
                        print(queues[u].peek().u)
                        print(queues[u].peek().v)
                        print(queues[u].peek().weight)
                    # Remove the edge from queues[u] if the adjacent
                    # vertex of u is already in T
                    queues[u].remove()
        
                if queues[u].isEmpty():
                    continue # Consider the next vertex in T
        
                # Current smallest weight on an edge adjacent to u
                edge = queues[u].peek()
                if edge.weight < smallestWeight:
                    v = edge.v
                    smallestWeight = edge.weight
                    # u is the parent for v 
                    parent[v] = u
    
            if v != -1: 
                T.append(v) # Add a new vertex to the tree
            else: 
                # The tree is not connected, a partial MST is found
                break 
          
            totalWeight += smallestWeight
    
        return MST(startingIndex, parent, T, 
                totalWeight, self.vertices)

    # Problem 23.1
    def getMinimumSpanningTree_Kruskals(self):
        numberOfVertices = len(self.vertices)

        # parent[v] stores the previous vertex of v in the path
        # The parent of source is set to -1
        parent = numberOfVertices * [-1]
        
        q = deepClone(self.queues)

        # sorting the weighted edges by weight
        sorted_by_weight = []
        for i in range(len(q)):
            while not(q[i].isEmpty()):
                a = q[i].remove()
                sorted_by_weight.append([a.weight, a.u, a.v])
        sorted_by_weight.sort()
        sorted_by_weight.reverse()
##        print(sorted_by_weight)
        
        a = sorted_by_weight.pop()
        sorted_by_weight.pop()
        
        vertices = self.vertices
        edges = [[a[1],a[2]],[a[2],a[1]]]
        T = [vertices[a[1]],vertices[a[2]]]
        totalweight = a[0]
        
        a = sorted_by_weight.pop()
        sorted_by_weight.pop()
##        print(a)
        edges.append([a[1],a[2]])
        edges.append([a[2],a[1]])
        for i in range(1,3):
            if vertices[a[i]] not in T:
                T.append(vertices[a[i]])
##        print(T)
        g = Graph(vertices, edges)
##        print(g.isCyclic())
##        print(g.vertices)
        totalweight += a[0]

        while len(T) < numberOfVertices or (not g.isConnected()):
            edge = sorted_by_weight.pop()
            sorted_by_weight.pop()
            if DEBUG:
                print('popped edge is', edge)
                print('sorted_by_weight =', sorted_by_weight)
            c = deepcopy(g)
##            c.addVertex(edge[1])
##            c.addVertex(edge[2])
            c.addEdge(vertices[edge[1]],vertices[edge[2]])
            c.addEdge(vertices[edge[2]],vertices[edge[1]])
            if DEBUG:
                print('1. T=',T)
##            try:
##            print(c.vertices)
##            print(c.neighbors)
            if not c.isCyclic(vertices[edge[1]]):
##                print('woo')
##                print('The graph is connected:', c.isConnected())

                for i in range (2):
##                    print('Check vertice in T')
##                    print('vertice:',vertices[edge[i+1]])
##                    print('T=',T)
                    if vertices[edge[i+1]] not in T:
                        T.append(vertices[edge[i+1]])
                    if DEBUG: print("T =", T)
                g = c
##                print(edge[0])
                totalweight += edge[0]
                if DEBUG:
                    print('totalweight:', totalweight)                                

                
        t = g.bfs(g.getIndex(T[0]))
        startingIndex = T[0]
        parent = t.parent
        searchOrders = t.searchOrders
        
        return MST(startingIndex, parent, searchOrders,
                   totalweight, vertices) 

    # Get a minimum spanning tree rooted at a specified vertex 
    def getMinimumSpanningTreeAt_Adj(self, startingIndex):
        # T initially contains the startingVertex;
        T = [startingIndex]
    
        numberOfVertices = len(self.vertices) # Number of vertices
        # Initially set the parent of all vertices to -1
        parent = numberOfVertices * [-1] # Parent of a vertex
    
        totalWeight = 0 # Total weight of the tree thus far
    
        # Clone the queues, so to keep the original queue intact
##        queues = deepClone(self.queues)
        matrix = create_bins(self.matrix)
##        print(matrix)
        # All vertices are found?
        while len(T) < numberOfVertices:
            # Search for the vertex with the smallest edge 
            # adjacent to a vertex in T
            v = -1
            smallestWeight = MAX_VALUE
            for u in T:
                try:
                    a = min(matrix[u])
                except:
                    continue
                while matrix[u] and (self.matrix[u].index(a) in T):
                    if DEBUG3: print(a)
                    matrix[u].remove(a)
                    if DEBUG3: print(matrix[u])
                    try:
                        a = min(matrix[u])
                    except:
                        pass
        
                if not matrix[u]: # i.e max(self.matrix[u]) == 0
                    continue # Consider the next vertex in T
        
                # Current smallest weight on an edge adjacent to u
                weight = min(matrix[u])
                vertice = self.matrix[u].index(weight)

##                weight = a
##                vertice = b
                if weight < smallestWeight:
                    v = vertice
                    smallestWeight = weight
                    # u is the parent for v 
                    parent[v] = u
    
            if v != -1: 
                T.append(v) # Add a new vertex to the tree
            else: 
                # The tree is not connected, a partial MST is found
                break 
          
            totalWeight += smallestWeight
    
        return MST(startingIndex, parent, T, 
                totalWeight, self.vertices)    
       
        
    # Find single source shortest paths 
    def getShortestPath(self, sourceIndex):
        # T stores the vertices whose path found so far
        T = [sourceIndex]
    
        numberOfVertices = len(self.vertices)
    
        # parent[v] stores the previous vertex of v in the path
        # The parent of source is set to -1
        parent = numberOfVertices * [-1]
    
        # costs[v] stores the cost of the path from v to the source
        # Initial cost set to infinity
        costs = numberOfVertices * [MAX_VALUE]
        costs[sourceIndex] = 0 # Cost of source is 0
    
        # Get a copy of queues
        queues = deepClone(self.queues)
    
        # Expand T
        while len(T) < numberOfVertices:
            v = -1 # Vertex to be determined
            smallestCost = MAX_VALUE # Set to infinity
            for u in T:
                while (not queues[u].isEmpty() and 
                           queues[u].peek().v in T):
                    # Remove the vertex in queue for u
                    queues[u].remove() 
            
                if queues[u].isEmpty():
                    # All vertices adjacent to u are in T
                    continue
        
                e = queues[u].peek()
                if costs[u] + e.weight < smallestCost:
                    v = e.v
                    smallestCost = costs[u] + e.weight
                    # now u is the parent for v
                    parent[v] = u
        
            T.append(v) # Add a new vertex to T
            costs[v] = smallestCost
    
        # Create a ShortestPathTree
        return ShortestPathTree(sourceIndex, parent, T, costs, 
                                self.vertices)

# Clone queues 
def deepClone(queues):
    copiedQueues = []

    for i in range(len(queues)):
        copiedQueues.append(Heap())
        for e in queues[i].getLst():
            copiedQueues[i].add(e)

    return copiedQueues

# MST is a subclass of Tree, defined in the preceding chapter
class MST(Tree):
    def __init__(self, startingIndex, parent, T, 
                 totalWeight, vertices):
        Tree.__init__(self, startingIndex, parent, T, vertices)
        # Total weight of all edges in the tree
        self.totalWeight = totalWeight 

    def getTotalWeight(self):
        return self.totalWeight

# ShortestPathTree is an inner class in WeightedGraph 
class ShortestPathTree(Tree):
    def __init__(self, sourceIndex, parent, T, costs, vertices):
        Tree.__init__(self, sourceIndex, parent, T, vertices)
        self.costs = costs

    # Return the cost for a path from the root to vertex v 
    def getCost(self, v):
        return self.costs[v]

    # Print paths from all vertices to the source 
    def printAllPaths(self):
        print("All shortest paths from " 
            + str(self.vertices[self.root]) + " are:")
        for i in range(len(self.costs)):
            self.printPath(i) # Print a path from i to the source
            print("(cost: " + str(self.costs[i]) + ")") # Path cost

def getEdges(edges):
    edgeList = []
            
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        # Insert an edge into the heap
        edgeList.append([u, v]) 
        
    return edgeList

def gen_matrix(edges):
    u = 0
    for i in edges:
        if u < i[0]:
            u = i[0]
##    print(u)
    # u contains the max number of nodes
    m = []
    for i in range (u+1):
        m.append([0]*(u+1))
##        print(m)
##    m[0][1] = 2
##    print(m)
    for u in edges:
##        print(u[0],u[1])
        m[u[0]][u[1]] = u[2]
##        print(m)
        
    return m

def create_bins(matrix):
    l = []
    for u in matrix:
        l.append([])
        for v in u:
            if v > 0:
                l[-1].append(v)

    return l
    

def main():
    # Create vertices
    vertices = ["Seattle", "San Francisco", "Los Angeles",
          "Denver", "Kansas City", "Chicago", "Boston", "New York",
          "Atlanta", "Miami", "Dallas", "Houston"]

    # Create edges
    edges = [
          [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
          [1, 0, 807], [1, 2, 381], [1, 3, 1267],
          [2, 1, 381], [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
          [3, 0, 1331], [3, 1, 1267], [3, 2, 1015], [3, 4, 599], 
            [3, 5, 1003],
          [4, 2, 1663], [4, 3, 599], [4, 5, 533], [4, 7, 1260],
            [4, 8, 864], [4, 10, 496],
          [5, 0, 2097], [5, 3, 1003], [5, 4, 533], 
            [5, 6, 983], [5, 7, 787],
          [6, 5, 983], [6, 7, 214],
          [7, 4, 1260], [7, 5, 787], [7, 6, 214], [7, 8, 888],
          [8, 4, 864], [8, 7, 888], [8, 9, 661], 
            [8, 10, 781], [8, 11, 810],
          [9, 8, 661], [9, 11, 1187],
          [10, 2, 1435], [10, 4, 496], [10, 8, 781], [10, 11, 239],
          [11, 8, 810], [11, 9, 1187], [11, 10, 239]
        ]

    # Create a graph
    graph1 = WeightedGraph(vertices, edges)
    a = graph1.getMinimumSpanningTree_Kruskals()
    b = graph1.getMinimumSpanningTreeAt(graph1.getIndex('Houston'))
    c = graph1.getMinimumSpanningTreeAt_Adj(graph1.getIndex('Dallas'))
    print(a.getTotalWeight())
    print(b.getTotalWeight())
    print(c.getTotalWeight())


main()

