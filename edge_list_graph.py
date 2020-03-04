# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:03:22 2020

@author: Simon
"""

class Vertex:    
    def __init__(self, e):
        self._element = e
    
    def __str__(self):
        return str(self._element)
    
    def element(self):
        return self._element
    
    def label(self):
        return str(self.label)
    
    def setLabel(self, l):
        self.label = l
    
        
class Edge:
    def __init__(self, e, v1, v2):
        self._element = e
        self._endpoints = [v1, v2]
    
    def __str__(self):
        return str(self._element)
    
    def element(self):
        return self._element
    
    def endpoints(self):
        return self._endpoints
    
    def label(self):
        return str(self.label)
    
    def setLabel(self, l):
        self.label = l

class Graph:

    def __init__(self):
        self._vertices = []
        self._edges = []
     
    #Inserts and returns a new vertex containing the element e.
    #Input: V; Output: Vertex    
    def insert_vertex(self, e):
        v = Vertex(e)
        self._vertices.append(v)
        return v
    
    #Removes the vertex v and all its incident edges
    #Input: Vertex; Output: nothing
    def remove_vertex(self, v):
        self._edges = [e for e in self._edges if v not in e.endpoints()]
        self._vertices.remove(v)
    
    #Inserts and returns a new edge between the vertices v and w. 
    #The element of the edge is o.    
    def insert_edge(self, o, v, w):
        e = Edge(o, v, w)
        self._edges.append(e)
        return e

    #Removes the edge e.
    #Input: Edge; Output: nothing
    def remove_edge(self, e):
        self._edges.remove(e)
    
    #Returns the count of vertices in the graph.
    #Input: nothing; Output: int
    def num_vertices(self):
        return len(self._vertices)
    
    #Returns the count of edges in the graph.
    #Input: nothing; Output: int
    def num_edges(self):
        return len(self._edges)
    
    #Returns an iterator on the vertices in the graph.
    #Input: nothing; Output: Iterator
    def vertices(self):
        return iter(self._vertices)
    
    #Returns an iterator on the edges in the graph.
    #Input: nothing; Output: Iterator
    def edges(self):
        return iter(self._edges)
    
    #Returns the degree of the vertex v.
    #Input: Vertex; Output: int
    def degree(self, v):
        d = 0
        for e in self._edges:
            if v in e._endpoints:
                d += 1
        return d
    
    #Returns an iterator on the vertices that are adjacent to v.
    #Input: Vertex; Output: Iterator
    def adjacent_vertices(self, v):
        a = []
        for e in self._edges:
            if v == e._endpoints[0]:
                a.append(e._endpoints[1])
            elif v == e._endpoints[1]:
                a.append(e._endpoints[0])
        return iter(a)
    
    #Returns an iterator on the edges that are incident to v. 
    #Input: Vertex; Output: Iterator
    def incident_edges(self, v):
        i = []
        for e in self._edges:
            if v in e._endpoints:
                i.append(e)
        return iter(i)
    
    #Returns a list with the two vertices at the ends of the edge e. 
    #Input: Edge; Output: list with 2 vertices
    def end_vertices(self, e):
        return e._endpoints[:]
    
    #Returns the vertex opposite v along the edge e.
    #Input: Vertex, Edge; Output: Vertex
    def opposite(self, v, e):
        if e._endpoints[0] == v:
            return e._endpoints[1]
        else:   
            return e._endpoints[0]
    
    #Returns whether the vertices v and w are adjacent.
    #Input: Vertex, Vertex; Output: boolean    
    def are_adjacent(self, v, w):
        for e in self._edges:
            if v in e._endpoints and w in e._endpoints:
                return True
        return False
    
    
class dfs_iterator:
    
    def __init__(self):
        self._graph = None
        self._visited = []
        
    def _dfs_visit(self, v):
        self._visited.append(v)
        for x in self._graph.adjacent_vertices(v):
            if x not in self._visited:
               self._dfs_visit(x)
                
    def iterator_dfs(self, g, v):
        self._graph = g
        self._visited = []
        self._dfs_visit(v)
        return iter(self._visited)

def is_connected(graph):
    dfs = dfs_iterator()
    visited = list(dfs.iterator_dfs(graph, 15))
    return len(visited) == graph.num_vertices()
    
def path(graph, v1, v2):
    dfs = dfs_iterator()
    visited = list(dfs.iterator_dfs(graph, v1))
    if v2 in visited:
        return True
    return False

def DFSS(g):
    for i in g.vertices():
        i.setLabel("UNEXPLORED")
    for i in g.edges():
        i.setLabel("UNEXPLORED")   
    for i in g.vertices():
        if i.label == "UNEXPLORED":
            DFS(g,i)
            
def DFS(g,v):
    v.setLabel("VISITED")
    for i in g.incident_edges(v):
        if (i.label == "UNEXPLORED"):
            w = g.opposite(v, i)
            if (w.label == "UNEXPLORED"):
                i.setLabel("DISCOVERY")
                DFS(g,w)
            else:
                i.setLabel("BACK")
    

vlist =[]
max=-1
counter =0
def findLargestElement(v: Vertex, graph: Graph):
    global vlist
    global max
    global counter
    counter +=1
    vlist.append(v)
    adj = graph.adjacent_vertices(v)
    if max < v:
        max = v
    for i in adj:
        if i not in vlist:
                findLargestElement(i,graph)
    
    return max

graph1 = Graph()
graph1.insert_vertex(15)
graph1.insert_vertex(6)
graph1.insert_vertex(38)
graph1.insert_vertex(66)
graph1.insert_vertex(123)
graph1.insert_vertex(160)
graph1.insert_edge(90,15,66)
graph1.insert_edge(23,15,6)
graph1.insert_edge(10,15,38)    
graph1.insert_edge(8,6,66)
graph1.insert_edge(7,6,123)
graph1.insert_edge(2,66,38)
graph1.insert_edge(76,66,123)
graph1.insert_edge(55,38,123)


v = next(graph1.vertices())



dfsVisitor = dfs_iterator()
visited = dfsVisitor.iterator_dfs(graph1, 6)

DFSS(graph1)
for v in graph1.vertices():
    print(v.label)

                
            
            
        