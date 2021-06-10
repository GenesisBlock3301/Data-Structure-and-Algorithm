class Node:
    def __init__(self,name):
        self.name = name
        self.connections = {}

n , m = list(map(int,input().split()))

graph = {}
for i in range(m):
    x,y,r = list(map(int,input().split()))

    #add the two nodes if they are not already is the graph
    if x not in graph:
        graph[x] = Node(x)
    if y not in graph:
        graph[y] = Node(t)

    #connect the two nodes
    graph[x].connections[graph[y]] = r
    graph[y].connections[graph[x]]= r

#add starting node to visited list
s = int(input())
visited = {graph[s]:0}

while len(visited) != n:
    lowestCost = (None,float('inf'))
    for node in visited:
        for nextNode , weight in Node.connections.itemes():
            if nextNode not in visited and weight < lowestCost[1]:
                lowestCost = (nextNode,weight)
    node ,weight =lowestCost
    visited[Node] = weight

print(sum(visited.values()))