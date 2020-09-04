class Graph:
    def __init__(self, nodes, directed=False):
        self.nodes=nodes
        self.directed=directed
        self.adj_list={}
        for node in nodes:
            self.adj_list[node]=[]

    def add_edge(self,u,v):
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if not self.directed:
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def degree(self,node):
        print("Degree of Node",node,"is :", end=" ")
        print(len(self.adj_list[node]))
        
    def print_adj_list(self):
        for node in self.nodes:
            print(node,':',self.adj_list[node])


print("**** NON DIRECTED GRAPH ****")
edges=[('A','B'),('A','C'),('B','C'),('B','D'),('D','E'),('C','E')]
nodes=['A','B','C','D','E','F']
graph=Graph(nodes)
print()

for u,v in edges:
    graph.add_edge(u,v)

graph.add_edge('A','F')
graph.add_edge('F','A')
graph.print_adj_list()
graph.degree('E')

print()
print()
print("**** DIRECTED GRAPH ****")
graph=Graph(nodes, True)
print()

for u,v in edges:
    graph.add_edge(u,v)

graph.add_edge('A','F')
graph.add_edge('F','A')
graph.print_adj_list()
graph.degree('E')
