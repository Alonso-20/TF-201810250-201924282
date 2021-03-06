import heapq as hq
from perlin_noise import PerlinNoise
import math

class Tools:
    def __init__(self):
        pass
    def distance(self, x, y, x1, y1):
        d = math.sqrt((x-x1)**2+(y-y1)**2)
        return d*100000

    def dijkstra(self, G, s, e):
        n = len(G)
        visited = [False]*n
        path = [-1]*n
        cost = [math.inf]*n
        cost[s] = 0
        pqueue = [(0, s)]
        while pqueue:
            g, u = hq.heappop(pqueue)
            if not visited[u]:
                visited[u] = True
                for v, w in G[u]:
                    if not visited[v]:
                        f = g + w
                        if f < cost[v]:
                            cost[v] = f
                            path[v] = u
                            hq.heappush(pqueue, (f, v))
        return path, cost

    def obtenerPath(self, i, path, zpath):
        if (i == -1):
            return list(reversed(zpath))
        zpath.append(i) 
        return Tools.obtenerPath(self, path[i], path, zpath)

    def remove(self, Gaux, i, j):
        r = []
        for k in range(len(Gaux[i])):
            if Gaux[i][k][0] == j:
                Gaux[i].pop(k)
                break

    def convert(adj, V):
        matrix = [[0 for j in range(V)] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                matrix[i][j[0]] = j[1]
        return list(matrix)
        
    def matrixPerlinNoiese(self, x, y):
        noise = PerlinNoise(octaves=1, seed=400)
        xpix, ypix = x, y
        pic = [[noise([i/xpix, j/ypix]) for j in range(700)] for i in range(700)]
        return pic