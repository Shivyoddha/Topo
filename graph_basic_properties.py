import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = np.array(*put_adjacency_matrix_here*)

# Create a graph from the adjacency matrix
G = nx.Graph(adjacency_matrix)

# Calculate average degree
average_degree = np.mean([deg for _, deg in G.degree()])

# Calculate network radius
network_radius = nx.radius(G)

# Calculate average hop count
average_hop_count = nx.average_shortest_path_length(G)

# Calculate network diameter
network_diameter = nx.diameter(G)

# Calculate node betweenness centrality
node_betweenness = nx.betweenness_centrality(G)
max_node_betweenness = max(node_betweenness.values())

# Calculate node closeness centrality
node_closeness = nx.closeness_centrality(G)

# Calculate degree assortativity
degree_assortativity = nx.degree_assortativity_coefficient(G)

# Calculate maximum degree
maximum_degree = max([deg for _, deg in G.degree()])

# Calculate number of nodes
number_of_nodes = G.number_of_nodes()

# Calculate number of links
number_of_links = G.number_of_edges()

# Calculate average clustering coefficient
clustering_coefficient = nx.average_clustering(G)

# Calculate algebraic connectivity
algebraic_connectivity = nx.algebraic_connectivity(G)

# Calculate link betweenness centrality
link_betweenness = nx.edge_betweenness_centrality(G)
max_link_betweenness = max(link_betweenness.values())

# Print the results
print("Average degree:", average_degree)
print("Network radius:", network_radius)
print("Average hop count:", average_hop_count)
print("Network diameter:", network_diameter)
print("Node betweenness (max):", max_node_betweenness)
print("Degree assortativity:", degree_assortativity)
print("Maximum degree:", maximum_degree)
print("Number of nodes:", number_of_nodes)
print("Number of links:", number_of_links)
print("Clustering coefficient:", clustering_coefficient)
print("Algebraic connectivity:", algebraic_connectivity)
print("Link betweenness (max):", max_link_betweenness)
