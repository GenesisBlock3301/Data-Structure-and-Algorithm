from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtils(self,v,visited):
        visited[v] = True
        print(v,end=" ")
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtils(i,visited)


    def DFS(self,v):
        visited = [False]*len(self.graph)
        self.DFSUtils(v,visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    print("Depth first search: ")
    g.DFS(2)
