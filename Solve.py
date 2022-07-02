import Graphy

class Solve:
    def __init__(self, traffic = False, time = 7):
        self.g = Graphy.Grapho()
        self.g.create()
        self.g.createAdjList(traffic, time)
        self.bRoute = []
        self.fARoute = []
        self.sARoute = []
        self.s = 0
        self.e = 0
        self.adjList = self.g.getAdj()
    def getAdj(self):
        return self.g.getAdj()
    def route(self, start, end):
        self.s = start
        self.e = end
        route = []
        #print("la primera ruta")  
        route, self.bRoute = self.g.bestRoute(start, end)
        return route, self.bRoute
    def firstAlernativeRoute(self):
        auxPath = []
        route = []
        route, self.fARoute = self.g.alternativeRoute(self.adjList, self.bRoute,self.s,self.e,auxPath)
        return route
    def secondAlternativeRoute(self):
        auxPath = []
        route, self.sARoute = self.g.alternativeRoute(self.adjList, self.fARoute,self.s,self.e,auxPath)
        return route
    def coordinates(self):
        return self.g.getCoordinate()
    def recreate(self):
        self.g.create()
        self.g.createAdjList()
        self.adjList = self.g.getAdj()
