import networkx as nx
from networkx.algorithms import bipartite
B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=0)
B.add_nodes_from(['a','b','c','d'], bipartite=1)
G = nx.Graph()
G.add_edge('A','B', weight = 4)
G.add_edge('A','B', weight = 4)
G.add_edge('A','B', weight = 4)

