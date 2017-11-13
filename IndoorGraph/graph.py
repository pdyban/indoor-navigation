
# coding: utf-8

# In[9]:


import networkx as nx
import json


# In[10]:


class Error(Exception):
    pass


# In[11]:


def compute_shortest_path(G, nodes):
    path = nx.dijkstra_path(G, nodes[0], nodes[1])
    return path


# In[17]:


def create_graph(path):
    G = nx.Graph()
    with open(path) as f:
        graph_dict = json.load(f, parse_int=str)
        G.add_weighted_edges_from(graph_dict)
    # G.add_edge(1, 2, weight=10)  # weight describes length in meters
    # G.add_edge(2, 3, weight=10)  # weight describes length in meters
    return G


# In[18]:


def test_this():
    G = create_graph('test_graph.json')
    path = compute_shortest_path(G, ('1','3'))
    path_graph = G.subgraph(path)
    assert path == ['1','2','3']


# In[20]:


# test_this()

