import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import numpy as np
G=nx.Graph()  # Create the default Graph object
G.add_node('f')  # add a node manually
G.add_node('g')  # add a node manually
G.add_edge('a', 'b', weight=0.6)  # Will add missing nodes and connecting edge
G.add_edge('a', 'c', weight=0.2)  # Will add missing nodes and connecting edge
G.add_edge('c', 'd', weight=0.1)  # Will add missing nodes and connecting edge
G.add_edge('c', 'e', weight=0.7)  # Will add missing nodes and connecting edge
G.add_edge('g', 'c', weight=0.8)  # Will add missing nodes and connecting edge
G.add_edge('f', 'a', weight=0.5)  # Will add missing nodes and connecting edge
pos = nx.layout.spring_layout(G)  # Try to optimize layout 
nx.draw(G, pos, with_labels=True, font_color="w", node_color="b")
plt.show()