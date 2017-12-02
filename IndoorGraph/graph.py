
# coding: utf-8

import networkx as nx
import json



class Error(Exception):
    pass


def compute_shortest_path(G, nodes):
    path = nx.dijkstra_path(G, nodes[0], nodes[1])
    return path


def create_graph(path):
    G = nx.Graph()
    with open(path) as f:
        js_graph = json.load(f)

        for node in js_graph['Knoten']:
            G.add_node(node['Id'], title=node['Titel'], position=(node['X'], node['Y'], node['Z']))

        # print(js_graph['Kanten'])
        for edge in js_graph['Kanten']:
            G.add_edge(edge['Knoten'][0], edge['Knoten'][1], weigth=edge['Länge'])

    return G


def test_this():
    G = create_graph('test_graph.json')
    path = compute_shortest_path(G, ('1','3'))
    path_graph = G.subgraph(path)
    assert path == ['1','2','3']


# In[20]:


# test_this()

