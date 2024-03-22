'''
22.13 (Induced subgraph) Given an undirected graph G = (V, E) and an integer k,
find an induced subgraph H of G of maximum size such that all vertices of H
have degree >= k, or conclude that no such induced subgraph exists. Implement
the method with the following header:
def maxInducedSubgraph(edge, k):
The method returns None if such subgraph does not exist.
'''
from Stack import Stack
from Queue import Queue
import copy
##import time

DEBUG = not True

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
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

        return Tree(u, parent, searchOrders, self.vertices)
# Returns a list of all the connected components of the graph
    def getConnectedComponents(self):
        s = set(self.vertices)
        l = []
        while s:
            i = s.pop()
            t = self.dfs(i)
            s = s.difference(set(t.searchOrders))
            l.append(t.searchOrders)
            
        return l

# A path between two vertices u and v. As BFS approach is being implemented, 
# the path obtained will be the shortest path between u and v.
    def getPath(self, u, v):
        t = self.bfs(v)
        l = t.getPath(self.getIndex(u))
        if len(l) == 1: # There is no path between u and v
            ret = None
        else:
            ret = l

        return ret

# Determine whether a graph is cyclic or not
    def isCyclic(self):
        rec_stack = len(self.vertices) * [False]
        
        # Mark visited vertices
        visited = len(self.vertices) * [False]
        
        # Recursively search
        for u in self.vertices:
            if self.isCyclicHelper(self.getIndex(u), visited, rec_stack):
                return True
        return False
# isCyclic helper function
    def isCyclicHelper(self, currentVertex, visited, rec_stack):
        if rec_stack[currentVertex]:
            return True
        if visited[currentVertex]:
            # Node has been already visited and has not resulted in a cycle
            # Thus return False
            return False

        visited[currentVertex] = True
        rec_stack[currentVertex] = True

        for i in self.neighbors[currentVertex]:
            if self.isCyclicHelper(i, visited, rec_stack):
                return True

        rec_stack[currentVertex] = False
        return False
    
##        visited[currentVertex] = True
##        rec_stack[currentVertex] = True 
##        for i in self.neighbors[currentVertex]:
##            # if the node is not visited
##            if not visited[i]:
##                # If the next recursive step returns True, pass it on
##                if self.isCyclicHelper(i, visited, rec_stack):
##                    return True
##            # if the current node has been visited earlier and is in rec_stack
##            elif rec_stack[i]:
##                return True
##
##        rec_stack[False]
##        return False

    # Determine whether a graph is cyclic or not
    def getACycle(self):
        if self.isCyclic():
            rec_stack = len(self.vertices) * [False]
            searchOrder = Stack()
            # Mark visited vertices
            visited = len(self.vertices) * [False]
            
            # Recursively search
            for u in self.vertices:
                if self.getACycleHelper(self.getIndex(u), visited, rec_stack, searchOrder):
                    return searchOrder
        else:
            return None
# isCyclic helper function
    def getACycleHelper(self, currentVertex, visited, rec_stack, searchOrder):
        if rec_stack[currentVertex]:
            return True
        if visited[currentVertex]:
            # Node has been already visited and has not resulted in a cycle
            # Thus return False
            return False

        visited[currentVertex] = True
        rec_stack[currentVertex] = True
        searchOrder.push(currentVertex)

        for i in self.neighbors[currentVertex]:
            if self.getACycleHelper(i, visited, rec_stack, searchOrder):
                return True

        rec_stack[currentVertex] = False
        searchOrder.pop()
        return False

# Determine whether the graph is bipartite or not
    def isBipartite(self):
        v = set(self.vertices) # a copy of self.vertices
        colours = [None] * len(self.vertices)
        a = False
        do_first_part = True
        while v: # while v is not empty
            if do_first_part:
            # This part will be done in two cases:
            # 1) When the function isBipartite is being called
            # 2) Everytime the set s which comprises of the neighbors of neighbors
            #    is empty. This cases deals with the case of the graph not being
            #    connected
                u = v.pop()
                if DEBUG:
                    print("Assigning", a, "to", u)
                colours[self.getIndex(u)] = a
                a = not a 
                neighbors = []+self.neighbors[self.getIndex(u)] # the neighbors list of u
                if DEBUG:
                    print("The neighbors of", u, "are:", neighbors)
                    print("The value of a is:", a)
            
            for i in neighbors:
                if colours[i] == None:
                    if DEBUG:
                        print(i, "is in the neighbor list of", u, "has not been assigned a state")
                        print("Assigning", a)
                    colours[i] = a
##                    v.remove(self.getVertex(i))
                    if DEBUG:
                        print("After having removed", i, "from v, the updated v is", v)
                elif colours[i] != a:
##                    print(i)
##                    print(colours[i],a)
                    if DEBUG:
                        print(i, "which was assigned the value of", colours[i], "is not equal to", a)
                    return False
                elif not (None in colours):     # All the nodes have been assigned a colour and there has
                    self.bipartite = colours    # not been a clash thus far
                    return True
                
##            print("Done")
            s = set()
##            print(neighbors)
            while neighbors:
                s = s.union(set(self.neighbors[neighbors.pop()])) # the set of neighbors of neighbors
                if DEBUG:
                    print("The new neighbors set is", s)
##                print(s)
            if s: # if s in not empty
                neighbors = list(s)
                a = not a
                do_first_part = False

            else: # when s is empty
                do_first_part = True

        self.bipartite = colours     
        return True

    def isBipartite_Shubha(self):
        v = set(self.vertices) # a copy of self.vertices
##        colours = [None] * len(self.vertices)
        a = True
        g1 = [] # set 1
        g2 = [] # set 2
        # Note: if a == True assign to g1, else to g2
        do_first_part = True
        while v:
            if do_first_part:
                u = self.getIndex(v.pop())
                if DEBUG:
                    print("The element being dealt with is:", u)
                check1 = False
                for i in range (len(g1)):
                    if u in self.neighbors[self.getIndex(g1[i])]:
                        check1 = True
                        break
                if check1:
                    check2 = False
                    for i in range (len(g2)):
                        if u in self.neighbors[self.getIndex(g2[i])]:
                            check2 = True
                            break
                    if check2: # u belongs to both g1 and g2 which means the graph is not bipartite
                        if DEBUG:
                            print(u, "belongs to both g1 and g2")
                            print("Exit 0")
                        return False
                    else:
                        a = False
                        g2.append(u)
                else:
                    a = True
                    g1.append(u)
            elif a:
                for i in range (len(g1)):
                    if u in self.neighbors[self.getIndex(g1[i])]:
                        if DEBUG:
                            print("We find", u, "to be in the neighbors list of", self.getIndex(g1[i]))
                            print("Exit 1")
                        return False
                g1.append(u)
                if DEBUG:
                    print("Assigning the current element", u, "to g1")
                    print("g1 is:", g1)
            else:
                for i in range (len(g2)):
                    if u in self.neighbors[self.getIndex(g2[i])]:
                        if DEBUG:
                            print("We find", u, "to be in the neighbors list of", self.getIndex(g2[i]))
                            print("Exit 2")
                        return False
                g2.append(u)
                if DEBUG:
                    print("Assigning the current element", u, "to g2")
                    print("g2 is:", g2)
            # finding the next node to look at
            a = not a
            
            found = False
##            print(self.getIndex(u))
##            print(self.neighbors)
            b = self.neighbors[self.getIndex(u)]
            if DEBUG:
                print("We'll now be selecting an element from the neighbors list of", u)
                print("The list is:", b)
            for i in b:
                if i in v:
                    u = i
##                    print(v,self.getVertex(u))
                    v.remove(self.getVertex(u))
                    if DEBUG:
                        print("The element", i, "in the neighbors list is in v")
                        print("The set v after having removed", u, "is:", v)
                    found = True
                break

            if not found: 
                do_first_part = True
            else:
                do_first_part = False
##        print(g1, g2)
        return True
    
    def getBipartite(self):
        if self.isBipartite():
            g1 = []
            g2 = []
            for i in range(len(self.bipartite)): # Defined at the end of isBipartite
                if self.bipartite[i]:
                    g1.append(i)
                else:
                    g2.append(i)
            ret = (set(g1),set(g2))
        else: ret = None

        return ret

    def maxInducedSubgraph(self, k):
        neighbors = copy.deepcopy(self.neighbors)
        vertices = copy.deepcopy(self.vertices)
        if DEBUG:
            print(vertices)
            print(neighbors)
        change = True
        while change:
            change = False
            for i in range (len(neighbors)):
                if (neighbors[i] != None and len(neighbors[i]) < k):
                    if DEBUG:
                        print("We are at node", vertices[i],
                              "with index", i)
                        print("Its neighbors list is:", neighbors[i])
                    change = True
                    v = neighbors[i]
                    for u in v:
                        neighbors[u].remove(i)
                    # remove the vertice from the list
                    vertices[i] = None
                    # remove the list of neighbors of the vertice
                    # which has less than k neighbors
                    neighbors[i] = None
                    if DEBUG:
                        print("Post operation we have:")
                        print("vertices:", vertices)
                        print("neighbors:", neighbors)
                    break
        edges = []
        new_vertices = []
        
        for u in vertices:
            if u != None:
                new_vertices.append(u)

        for i in range (len(new_vertices)):
            for u in neighbors[self.getIndex(new_vertices[i])]:
                edges.append([i, new_vertices.index(vertices[u])])
                
        if not new_vertices: # if vertices is empty
            ret = None
        else:
            ret = Graph(new_vertices, edges)

        return ret
                  
            
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
##    edges = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3],
##             [2, 4], [3, 1], [3, 2], [3, 4], [3, 5], [4, 2],
##             [4, 3], [4, 5], [5, 3], [5, 4]]
##    edges = [[0,1], [0,2], [0,3], [1,0], [1,3], [2,0], [2,3],
##             [3,0], [3,1], [3,2], [4,5], [5,4]]
##    edges = [[0,1], [1,2], [2,3], [3,0]]
##    edges = [[0,1],[0,2],[0,3],[4,1],[4,2],[4,3],[1,0],[1,4],
##             [2,0],[2,4],[3,0],[3,4]]
    edges = [[0,1], [1,0], [1,2], [2,1], [2,3], [2,4], [2,5],
             [3,2], [3,4], [3,5], [4,2], [4,3], [4,5], [5,2],
             [5,3], [5,4]]
    vertices = [0,1,2,3,4,5]
##    vertices = [4,3,2,1,0]
##    vertices = [0,1,2,3]
    g = Graph(vertices, edges)
##    print(g.getConnectedComponents())
##    print(g.getPath(1,3))
##    print(g.isCyclic())
##    print(g.getACycle())
##    print(g.neighbors)
##    t1 = time.time()
##    print(g.isBipartite())
##    t2 = time.time()
##    print("Time:", round(t2-t1,5))
##    print(g.neighbors)
##    t1 = time.time()
##    print(g.isBipartite_Shubha())
##    t2 = time.time()
##    print("Time:", round(t2-t1,5))
##    print(g.neighbors)
    h = g.maxInducedSubgraph(3)
    if h:
        print(h.vertices)
        print(h.neighbors)
    else:
        print(h)
##    print(g.getBipartite())
if __name__ == "__main__":
    main()


    
