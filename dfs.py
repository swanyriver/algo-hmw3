WHITE = 1
GRAY = 2
BLACK = 3

class vertex():
    """docstring for ClassName"""
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.color = WHITE
        self.predecesor = None
        self.discovertime = None
        self.finishtime = None

a = vertex('a')
b = vertex('b')
c = vertex('c')
d = vertex('d')
e = vertex('e')
f = vertex('f')
g = vertex('g')
h = vertex('h')

G = [a,b,c,d,e,f]

a.adj = [c,e,b]
b.adj = [e,d]
c.adj = [e]
d.adj = [c,f,e]
e.adj = [f]



time = 0

def DFS(g):
    global time
    time = 0
    for u in g:
        if u.color == WHITE:
            DFSVisit(u)

def DFSVisit(u):
    global time
    time = time+1
    u.discovertime = time
    u.color = GRAY

    for v in u.adj:
        if v.color == WHITE:
            v.predecesor = u
            DFSVisit(v)

    u.color = BLACK
    time = time + 1
    u.finishtime = time

DFS(G)

for v in G:
    print v.name, "d:" , v.discovertime , "f:", v.finishtime, "pred: ", v.predecesor.name if v.predecesor else "none"
G.sort(key=lambda x:x.finishtime, reverse=True)
print [v.name for v in G]

print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"


a = vertex('a')
b = vertex('b')
c = vertex('c')
d = vertex('d')
e = vertex('e')
f = vertex('f')
g = vertex('g')
h = vertex('h')

a.adj = [d]
b.adj = [d,c]
c.adj = [d,e]
d.adj = []
e.adj = [h]
f.adj = [g,e]
g.adj = [h]
h.adj = []

G = [a,b,c,d,e,f,g,h]


DFS(G)

for v in G:
    print v.name, "d:" , v.discovertime , "f:", v.finishtime, "pred: ", v.predecesor.name if v.predecesor else "none"
G.sort(key=lambda x:x.finishtime, reverse=True)
print [v.name for v in G]
print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"


a = vertex('a')
b = vertex('b')
c = vertex('c')
d = vertex('d')
e = vertex('e')
f = vertex('f')
g = vertex('g')
h = vertex('h')

a.adj = [b]
b.adj = [c]
c.adj = [d,a]
d.adj = [e]
e.adj = [c]

G = [a,b,c,d,e]


DFS(G)

for v in G:
    print v.name, "d:" , v.discovertime , "f:", v.finishtime, "pred: ", v.predecesor.name if v.predecesor else "none"
G.sort(key=lambda x:x.finishtime, reverse=True)
print [v.name for v in G]
