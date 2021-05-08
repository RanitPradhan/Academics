class adjacentlist:
    def __init__(self):
        self.List = {}
    def addedge(self, source, dest):
        if source in self.List.keys():
            self.List[source].append(dest)
        else:
            self.List[source] = [dest]
    def printgraph(self):
        for i  in self.List:
            print('Vertex ',i)
            print(i,'->',' -> '.join([str(j) for j in self.List[i]]))

n = adjacentlist()
n.addedge('A', 'B')
n.addedge('A', 'C')
n.addedge('B', 'E')
n.addedge('B', 'D')
n.addedge('D', 'E')
n.addedge('C', 'D')
n.addedge('D', 'A')
n.printgraph()


