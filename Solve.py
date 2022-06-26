import Graphy

class Solve:
    def __init__(self):
        self.g = Graphy.Grapho()
        self.g.create()
        self.g.createAdjList()
    def getAdjList(self):
        return self.g.getAdjList()
    def route(self, start, end):
        print("la primera ruta")        
        return self.g.bestRoute(start, end)
    def firstAlernativeRoute(self):

        return
    def secondAlternativeRoute(self):
        return
    def coordinates(self):
        return
