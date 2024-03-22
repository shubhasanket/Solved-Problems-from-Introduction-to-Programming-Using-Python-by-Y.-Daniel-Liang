'''22.1 (Test whether a graph is connected) Write a program
that reads a graph from a file and determines whether the graph
is connected. The first line in the file contains a number that
indicates the number of vertices (n). The vertices are labeled
as 0, 1, ..., n-1. Each subsequent line, with the format u v1 v2 ...,
describes edges (u, v1), (u, v2), and so on.
Your program should prompt the user to enter the name of the file,
should read data from a file, create an instance g of Graph, invoke
g.printEdges() to display all edges, and invokes dfs() to obtain an
instance tree of Tree. If tree.getNumberOfVerticeFound() is the same
as the number of vertices in the graph, the graph is connected.
'''
from Graph import Graph
from Graph import Tree
def main():
    file = input("Enter a file name: ")
    file = "file.txt"
    inf = open(file, "r")
    line = inf.readline()
    num_vertices = eval(line)
    print("The number of vertices is:", num_vertices)
    ##print(eval(num_vertices), type(num_vertices))
    
    vertices = [("Vertex "+str(i)) for i in range (num_vertices)]
    ##print(vertices)
    edges = []
    line = inf.readline().strip()
    while line != "":
##        print(".")
        l = line.split(" ")
        a = eval(l.pop(0))
        for x in l:
            edges.append([a,eval(x)])
    ##    print(edges)
        line = inf.readline().strip()
    #creating an instance of Graph
    print(edges)
    g = Graph(vertices, edges)
    g.printEdges()
    t = g.dfs(0)
    print(t.parent)
    print(t.searchOrders)
    if t.getNumberOfVerticesFound() == len(vertices):
        print("The graph is connected")
    else:
        print("The graph is not connected")
    
if __name__ == "__main__":
    main()










    
    
