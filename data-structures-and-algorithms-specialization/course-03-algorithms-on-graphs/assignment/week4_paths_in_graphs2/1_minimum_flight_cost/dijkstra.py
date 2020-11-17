#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #write your code here
    q = queue.PriorityQueue()
    
    inf = 0
    for obj in cost:
        inf += sum(obj)
    inf += 1
    dist = [inf] * len(adj)
    dist[s] = 0
    
    for v in range(len(adj)):
        q.put((dist[v], v))
        
    while not q.empty():
        u = q.get()[1]
        for i in range(len(adj[u])):
            v = adj[u][i]
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                q.put((dist[v], v))
    if dist[t] == inf:
        return -1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
