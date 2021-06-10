def BFS(s):
    queue = []
    queue.append(s)
    visited[s] = True
    dist[s] = 0
    while queue:
        s = queue.pop(0)
        for i in graph[s]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                dist[i] = dist[s]+1



if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n , m = map(int,input().split())
        graph = [[] for x in range(n)]
        dist = [-1 for x in range(n)]
        visited = [False for x in range(n)]
        for _ in range(m):
            u,v = map(lambda x: int(x)-1,input().split())
            graph[u].append(v)
            graph[v].append(u)
        s = int(input()) - 1
        BFS(s)
        # print(dist)
        for i in range(n):
            if i == s:
                continue
            if dist[i] != -1:
                print(dist[i]*6,end=" ")
            else:
                print(-1,end=" ")
        print()
