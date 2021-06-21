import pandas as pd
import networkx as nx
import pygraphviz
from graphviz import Source
path = '/Users/mattiafumagalli/Desktop/anti-patterns-learning/last.dot'
g = nx.drawing.nx_agraph.read_dot(path)
s = Source.from_file(path)
s.view()
print(s)


