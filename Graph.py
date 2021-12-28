import sys

class Graph:
    from collections import defaultdict

    def __init__(self, Vertices = None):
        self.graph = Graph.defaultdict(list)
        self.vertex = Vertices
        self.matrix = [[0 for column in range(Vertices)] 
                        for row in range(Vertices)]
        self.vector = []


    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    
    def BreadthFirstSearch(self, Index):
        Visited = [0 for _ in range(max(self.graph) + 1)]
        Queue = []
        Visited[Index] = 1
        Queue.append(Index)

        while Queue:
            Index = Queue.pop(0)
            print(f"BFS-Visited Vertex :- {Index}","\n")
            for i in self.graph[Index]:
                if Visited[i] == 0:
                    Queue.append(i)
                    Visited[i] = 1
    
    def DepthFirstSearchHelper(self, v, visited):
        visited.add(v)
        print(f"DFS-Visited Vertex :- {v}","\n")
        for Next in self.graph[v]:
            if Next not in visited:
                self.DepthFirstSearchHelper(Next, visited)
    
    def DepthFirstSearch(self, Index):
        Visited = set()
        self.DepthFirstSearchHelper(Index, Visited)

    def DisplayGraph(self):
        print(f"Graph is :- {self.graph}")
    
    def DisplayPrims(self, parent):
        print("EDGE \tWeight")
        MinCost = 0
        for i in range(1, self.vertex):
            MinCost += self.matrix[i][parent[i]]
            print(parent[i], "-", i, "\t", self.matrix[i][parent[i]])
        print("Minimum Spanning Tree" , MinCost)
    
    def MinKey(self,key, mstSet):
        min = sys.maxsize

        for v in range(self.vertex):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                MinIndex = v
        return MinIndex
    
    def PrimsMST(self):
        key = [sys.maxsize for _ in range(self.vertex)]
        parent = [None for _ in range(self.vertex)]

        key[0] = 0
        mstSet = [False for _ in range(self.vertex)]
        parent[0] = -1

        for _ in range(self.vertex):
            u = self.MinKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.vertex):
                if self.matrix[u][v] > 0 and mstSet[v] == False and key[v] > self.matrix[u][v]:
                    key[v] = self.matrix[u][v]
                    parent[v] = u
        self.DisplayPrims(parent)
    
    def DisplayKruskal(self,result):
        MinCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            MinCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , MinCost)

    def KruskalEdge(self,u, v, w):
        self.vector.append([u,v,w])

    def Find(self, parent, i):
        if parent[i] == i:
            return i
        return self.Find(parent, parent[i])
    
    def Union(self, parent, rank, x, y):
        xRoot = self.Find(parent,x)
        yRoot = self.Find(parent, y)

        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1
        
    def KruskalMST(self):
        result = []
        i = 0                    # An index variable, used for sorted edges
        e = 0                    # An index variable, used for result[]

        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph  
        self.vector =  sorted(self.vector, key = lambda item : item [2])
        parent = []
        rank = []

        for Node in range(self.vertex):
            parent.append(Node)
            rank.append(0)
        
        while e < self.vertex - 1 :

            u,v,w = self.vector[i]
            i += 1
            x = self.Find(parent, u)
            y = self.Find(parent,v)

            if x != y:
                e += 1
                result.append([u,v,w])
                self.Union(parent, rank, x, y)

        self.DisplayKruskal(result)

















if __name__ == "__main__":
    G = Graph(Vertices = 5)
    G.matrix = [[0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]]
    G.PrimsMST()
    # G.KruskalEdge(0,1,10)
    # G.KruskalEdge(0,2,6)
    # G.KruskalEdge(0,3,5)
    # G.KruskalEdge(1,3,15)
    # G.KruskalEdge(2,3,4)

    # G.KruskalMST()

