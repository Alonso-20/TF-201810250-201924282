import Graphy

class Solve:
    def __init__(self):
        self.g = Graphy.Grapho()
        self.g.create()
        self.g.createAdjList()
        self.bRoute = []
        self.fARoute = []
        self.s = 0
        self.e = 0
        self.adjList = self.g.getAdjList()
    def getAdjList(self):
        return self.g.getAdjList()
    def route(self, start, end):
        self.s = start
        self.e = end
        print("la primera ruta")  
        self.bRoute = self.g.bestRoute(start, end)
        return self.g.bestRoute(start, end)
    def firstAlernativeRoute(self):
        auxPath = []
        self.fARoute = self.g.alternativeRoute(self.adjList, self.bRoute,self.s,self.e,auxPath)
        return self.fARoute
    def secondAlternativeRoute(self):
        auxPath = []
        return self.g.alternativeRoute(self.adjList, self.fARoute,self.s,self.e,auxPath)
    def coordinates(self):
        return
