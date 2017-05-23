import networkx as nx
G=nx.Graph()
G.add_node("spam")
G.add_edge(1,2)

H=nx.path_graph(10)
G.add_nodes_from(H)


G.add_edge(1,2)
e=(2,3)
G.add_edge(*e) # unpack edge tuple*


G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam")       # adds node "spam"
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'


import matplotlib.pyplot as plt
nx.draw(G)
nx.draw_random(G)
nx.draw_circular(G)
nx.draw_spectral(G)

nx.draw(G)