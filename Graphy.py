import csv
import Tools

class Grapho:
    def __init__(self):
        self.t = Tools.Tools()
        self.nodos = []
        self.pnodos = []
        self.adjList = []
        shortRoute = []
        firstAlternativeRoute = []
        secondAlternativeRoute = []
    def create(self,path = 'DataSet_Nodos_lat_lon_+1000.csv' ):
        with open(path) as archivo:
            add = set()
            lector = csv.reader(archivo)
            head = next(lector)
            if head is not None:
                for row in lector:
                    id,c1,c2,x,y=row
                    if not f"{c1},{c2}" in add and not c1 == c2:
                        add.add(f"{c1},{c2}")
                        add.add(f"{c2},{c1}")
                        add.add(f"{c1},{c1}")
                        self.nodos.append([c1,c2,float(x),float(y)])
                        self.pnodos.append([c1,c2])
    
    
    def createAdjList(self):
        cont = 0
        flag0 = True
        flag1 = True
        for i in range(len(self.nodos)):
            self.adjList.append([])
        for i in range(len(self.nodos) - 1):
            for j in range(i , len(self.nodos) - 1):
                #while(cont < 2):
                if flag0 and self.nodos[i][0] == (self.nodos[j + 1][0] or self.nodos[j + 1][1]):
                    d = self.t.distance(self.nodos[i][2], self.nodos[i][3],self.nodos[j + 1][2], self.nodos[j + 1][3])
                    self.adjList[i].append([j + 1,d])
                    self.adjList[j + 1].append([i, d])
                    flag0 = False
                if flag1 and self.nodos[i][1] == (self.nodos[j + 1][1] or self.nodos[j + 1][0]):
                    d = self.t.distance(self.nodos[i][2], self.nodos[i][3],self.nodos[j + 1][2], self.nodos[j + 1][3])
                    self.adjList[i].append([j + 1,d])
                    self.adjList[j + 1].append([i, d])
                    flag1 = False
                #m.append(0)
            # cont += 1
            #cont = 0
            flag0 = True
            flag1 = True
        #matriz.append(m)
        #m=[]
    def bestRoute(self, start, end):
        auxPath = []
        Opath, cost = self.t.dijkstra(self.adjList, start, end)
        self.shortRoute = self.t.obtenerPath(end, Opath, auxPath)
        return self.shortRoute
    def alternativeRoute(self, path, start, end, auxPath):
        nPath = []
        #print(nPath)
        copyG = self.adjList
        copyPath = path
        limit = int(len(copyPath)*0.3)
        for i in range(len(copyPath) - 1):
            s = copyPath[i]
            e = copyPath[i + 1]
            if i > limit and i < len(copyPath) - limit:
                #print(f"Eliminar de {s} a {e} ?")
                self.t.remove(copyG, s, e) 
                #print(f"Eliminar de {e} a {s} ?")
                self.t.remove(copyG, e, s)
        #print(copyG)
        OnewPath, newCost = self.t.dijkstra(copyG, start, end)
        #print(OnewPath)
        return self.t.obtenerPath(self, end, OnewPath, auxPath)

    def getNodos(self):
        return self.nodos
    def getAdjList(self):
        return self.adjList
