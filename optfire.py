class vertex():
    """docstring for vertex"""
    def __init__(self, name):
        self.name = name
        self.adj = []

class edge(object):
    """docstring for edge"""
    def __init__(self, connects, weight):
        self.connects = connects
        self.weight = weight

def makeedge(v1, v2, w):
    v1.adj.append(edge(v2,w))
    v2.adj.append(edge(v1,w))

a = vertex('a')
b = vertex('b')
c = vertex('c')
d = vertex('d')
e = vertex('e')
f = vertex('f')
g = vertex('g')
h = vertex('h')

G = [a,b,c,d,e,f,g,h]

makeedge(a,c,4)
makeedge(a,f,7)
makeedge(c,d,3)
makeedge(c,g,9)
makeedge(c,f,2)
makeedge(f,g,8)
makeedge(d,g,7)
makeedge(d,e,3)
makeedge(g,e,2)
makeedge(g,h,3)
makeedge(e,b,9)
makeedge(e,h,7)
makeedge(h,b,3)

def optimalfire(g):
    best_location = None
    best_distance = float('inf')

    for s in g:
        longest = Dijkstra(g,s, best_distance)
        if longest<best_distance:
            best_distance = longest
            best_location = s

    return best_location

def Dijkstra(g,s,best):
    for v in g:
        v.d = float('inf')

    s.d = 0

    max_distance = float('-inf')

    q = list(g)

    while q:
        u = min(q, key= lambda x:x.d)
        q.remove(u)

        if u.d > max_distance:
            max_distance = u.d
            if max_distance >= best: return max_distance

        for e in u.adj:
            w = e.weight
            v = e.connects

            if v.d > u.d + w: v.d = u.d + w

    return max_distance


best = optimalfire(G)

dist = Dijkstra(G,best,float('inf'))

print "best source is:",best.name, "  with a longest distance of:", dist
print [v.name + ":" + str(v.d) for v in G]

for v in G:
    print v.name, " = ",v.d, " from fires station"


