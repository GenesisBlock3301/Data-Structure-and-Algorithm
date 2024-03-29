from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False]*(max(self.graph))
        print(len(self.graph),visited)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s,end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(2,5)
    g.addEdge(5,3)
    g.addEdge(5,6)
    g.addEdge(3,4)
    # g.addEdge(3,3)
    print("Breath first search: ")
    g.BFS(2)
