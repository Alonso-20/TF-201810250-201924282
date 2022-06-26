import json
import Solve

g = Solve.Solve()
def graph():
    Loc = g.coordinates()
    G = g.getAdjList()

    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    bestpath = g.route()
    path1 = g.firstAlernativeRoute()
    path2 = g.secondAlternativeRoute()

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)

