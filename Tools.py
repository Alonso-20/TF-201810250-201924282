import heapq as hq
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
        #print(f"nodo: {i} y padre {path[i]}")
        zpath.append(i) 
        return Tools.obtenerPath(self, path[i], path, zpath)
    def remove(self, Gaux, i, j):
        r = []
        #cambiar a indexadeo
        for k in range(len(Gaux[i])):
            #print(f"{Gaux[i][k][0]} es igual a {j} ?")
            if Gaux[i][k][0] == j:
                Gaux[i].pop(k)
                #np.delete(Gaux[i],k)
                    #del G[i][j]
                #print(f"Se ah quitado {Gaux[i][k]} de {Gaux[i]}")
                #print(f"Resultado: {Gaux[i]}")
                break
        