import json
import random as r
import math
import heapq as hq
import Solve


s = Solve.Solve()
G = s.getAdj()
Loc = s.coordinates()

def graph():
    return json.dumps({"loc": Loc, "g": G})


def paths(start, t):
    
    bestpath = s.route(start, t)
    path1 = s.firstAlernativeRoute()
    path2 = s.secondAlternativeRoute()
    s.__init__()
    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})
