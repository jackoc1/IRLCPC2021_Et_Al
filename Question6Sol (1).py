class Vertex:
    def __init__(self, elt):
        self.elt = elt

    def getElement(self):
        return self.elt

    def __str__(self):
        return str(self.elt)


class Edge:
    def __init__(self, v1, v2, elt):
        self.v1 = v1
        self.v2 = v2
        self.elt = elt

    def vertices(self):
        return (self.v1, self.v2)

    def opposite(self, x):
        if self.v1 == x:
            return self.v2
        elif self.v2 == x:
            return self.v1
        else:
            return None

    def getElement(self):
        return str(self.elt)

    def __str__(self):
        return str([str(self.v1), str(self.v2), str(self.elt)])

    def getVertex1(self):
        return self.v1

    def getVertex2(self):
        return self.v2

class Graph:
    def __init__(self):
        self.vertexDict = {}
        self.vertexElt = {}
    

    def vertices(self):
        return self.vertexDict.keys()

    def edges(self):    
        edges = set()
        for dict in self.vertexDict.values():
            for edge in dict.values():
                edges.add(edge)
        return list(edges)


    def num_vertices(self):
        return len(self.vertexDict)

    def num_edges(self):    
        return len(self.edges())

    def get_edge(self, x,y):
        try:
            dictX = self.vertexDict[x]
            edge = dictX[y]
            return edge
        except:
            return None
        
    def degree(self, x):
        return len(self.vertexDict[x])

    def get_edges(self, x):
        try:
            dictX = self.vertexDict[x]
            return list(dictX.values())
        except:
            return []
    
    def add_vertex(self, elt):
        v = Vertex(elt)
        self.vertexDict[v] = {}
        self.vertexElt[elt] = v
        return v
    

    def add_edge(self, x, y, elt):
        if x not in self.vertices() or y not in self.vertices():
            return None
        edge = Edge(x,y,elt)
        self.vertexDict[x][y] = edge
        self.vertexDict[y][x] = edge
        return edge

    def remove_vertex(self, x):
        try:
            dictX = self.vertexDict[x]
            neighbours = dictX.keys()
            for vertex in neighbours:
                self.vertexDict[vertex].pop(x)
            self.vertexDict.pop(x)
        except:
            pass

    
    def remove_edge(self, e):
        x = e.v1
        y = e.v2

        try:
            dictX = self.vertexDict[x]
            dictX.pop(y)
            dictY = self.vertexDict[y]
            dictY.pop(x)
        
        except:
            pass

    def __str__(self):
        if self.num_vertices() > 100:
            return "String too long"
        out = ""
        for vertex, edges in self.vertexDict.items():
            out = out + str(vertex) + " : " + str([str(edge) for edge in edges.values()]) + "\n"
        return out 
        

    
    def get_vertex_by_label(self, element):
        try:
            return self.vertexElt[element]
        except:
            return None


    def highestdegree(self):
        maxDegree = 0
        vertices = []
        for v in self.vertexDict.keys():
            if self.degree(v) > maxDegree:
                maxDegree = self.degree(v)
                vertices.append(v)


    def depthfirstsearch(self, v): 

        marked = {v:None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)


class Element:
    def __init__(self, k, v, i):
        self.key = k
        self.value = v
        self.index = i

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def _wipe(self):
        self.key = None
        self.value = None
        self.index = None

    def __str__(self):
        return "(%s, %s, %d)" %(str(self.key), str(self.value), self.index)





class APQ:
    def __init__(self):
        self.heap = []

    
    def add(self, key, item):
        i = len(self.heap)
        e = Element(key, item, i)
        self.heap.append(e)
        self.bubbleUp(i)
        return e


    def max(self):
        if len(self.heap) > 0:
            return self.heap[0].value

    
    def remove_max(self):
        if self.length() ==  1:
            m = self.heap[0]
            self.heap.pop()
            return m
        elif self.length() > 1:
            m = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self.heap[0].index = 0
            self.bubbleDown(0)
            return m


    def update_key(self, element, newkey):
        oldkey = element.key
        element.key = newkey
        i = element.index
        if newkey < oldkey: #then don't have to bubble up 
            self.bubbleDown(i)
        else:
            self.bubbleUp(i)


    def get_key(self, element):
        return element.key


    def remove(self, element):
        i = element.index
        oldkey = element.key
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.heap.pop()
        self.heap[i].index = i
        newkey = self.heap[i].key
        if newkey < oldkey:
            self.bubbleDown(i)
        else:
            self.bubbleUp(i)


    def bubbleUp(self, i):
        inlist = self.heap
        while i > 0:
            parent = (i-1) // 2
            if inlist[i] > inlist[parent]:
                # print('swapping:', inlist[i], 'with its parent:', inlist[parent])
                inlist[i], inlist[parent] = inlist[parent], inlist[i]
                self.heap[i].index = i
                self.heap[parent].index = parent
                i = parent
            else:
                i = 0


    def bubbleDown(self, i):
        inlist = self.heap
        last = len(self.heap)
        while last > (i*2 + 1):  #so at least one child
            lc = i*2 + 1
            rc = i*2 + 2
            maxc = lc   # start by assuming left child is the max child
            if last > rc and inlist[rc] > inlist[lc]:  #rc exists and is bigger
                maxc = rc
            if inlist[i] < inlist[maxc]:
                inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
                i = maxc
                self.heap[i].index = i
                self.heap[maxc].index = maxc
            else:
                i = last

    def length(self):
        return len(self.heap)


    def __str__(self):
        return str([str(v) for v in self.heap])     



def prim(G):
    # out = []
    out = Graph()
    free = {}
    locs = {}       #vertex: key
    pq = APQ()     #{cost: (vertex, edge)}


    for vertex in G.vertices():
        key = pq.add(0, vertex)
        locs[vertex] = key

        free[vertex] = None
    

    while pq.length() > 0:
        elt = pq.remove_max() #c:(v)
        v = elt.value
        e = free[v]
        free.pop(v)
        locs.pop(v)
        if e != None:
            v1 = out.add_vertex(e.v1.elt)
            v2 = out.add_vertex(e.v2.elt)
            out.add_edge(v1, v2, e.elt)
        for edge in G.get_edges(v):
            w = edge.opposite(v)
            if w in free:
                wElt = locs[w]
                cost = edge.elt
                if w in free:
                    oldcost = pq.get_key(wElt)
                    if cost > oldcost:
                        pq.update_key(wElt, cost)
                        free[w] = edge

    return out



num_exchanges = int(input())

# graphs = [Graph() for i in range(num_exchanges)]
graphs = {}

for i in range(1, num_exchanges+1):
    graphs[i] = Graph()


for graph in graphs.values():
    num_junctions, num_edges = tuple(map(int, input().split()))

    for i in range(num_edges):

        a, b, w = tuple(map(int, input().split()))
        v1 = graph.get_vertex_by_label(a)
        v2 = graph.get_vertex_by_label(b)

        if v1 == None:
            v1 = graph.add_vertex(a)

        if v2 == None:
            v2 = graph.add_vertex(b)


        graph.add_edge(v1, v2, w)




max_trees_path = {}
for indx, graph in graphs.items():
    max_trees_path[indx] = prim(graph)

        


g = max_trees_path[4]


dict = {}
for ind, tree in max_trees_path.items():
    cost = []
    v = tree.get_vertex_by_label(ind)
    for edge in tree.get_edges(v):
        c = edge.elt 
        cost.append(c)
    dict[min(cost)] = ind


m = min(dict.keys())
source = dict[m]
if source == num_exchanges:
    drain = 1
else:
    drain = source + 1

dict.pop(m)

new_m = min(dict.keys())
dict.pop(new_m)

new_min = min(dict.keys())

print(source, drain, new_min)
          