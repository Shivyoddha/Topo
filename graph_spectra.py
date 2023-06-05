import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = np.array(*put the adjacency matrix here*)

# Create a graph from the adjacency matrix
graph = nx.from_numpy_array(adjacency_matrix)

# Calculate Resistance Distance Spectra
laplacian_matrix = np.diag(np.sum(adjacency_matrix, axis=1)) - adjacency_matrix
resistance_distance_spectrum = np.sort(np.linalg.eigvalsh(np.linalg.pinv(laplacian_matrix)))

# Calculate Distance Spectra
distance_matrix = nx.floyd_warshall_numpy(graph)
distance_spectrum = np.sort(np.linalg.eigvalsh(distance_matrix))

# Calculate Signless Laplacian Spectra
signless_laplacian_matrix = adjacency_matrix + np.diag(np.sum(adjacency_matrix, axis=1))
signless_laplacian_spectrum = np.sort(np.linalg.eigvalsh(signless_laplacian_matrix))

# Calculate Normalized Laplacian Spectra
degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
normalized_laplacian_matrix = np.linalg.inv(np.sqrt(degree_matrix)) @ laplacian_matrix @ np.linalg.inv(np.sqrt(degree_matrix))
normalized_laplacian_spectrum = np.sort(np.linalg.eigvalsh(normalized_laplacian_matrix))

# Calculate Adjacency Spectra
adjacency_spectrum = np.sort(np.linalg.eigvalsh(adjacency_matrix))

# Plot the spectra
plt.figure(figsize=(10, 6))

# Resistance Distance Spectra
plt.subplot(231)
plt.plot(resistance_distance_spectrum, 'b')
plt.title('Resistance Distance Spectra')

# Distance Spectra
plt.subplot(232)
plt.plot(distance_spectrum, 'g')
plt.title('Distance Spectra')

# Signless Laplacian Spectra
plt.subplot(233)
plt.plot(signless_laplacian_spectrum, 'r')
plt.title('Signless Laplacian Spectra')

# Normalized Laplacian Spectra
plt.subplot(234)
plt.plot(normalized_laplacian_spectrum, 'm')
plt.title('Normalized Laplacian Spectra')

# Adjacency Spectra
plt.subplot(235)
plt.plot(adjacency_spectrum, 'c')
plt.title('Adjacency Spectra')

plt.tight_layout()
plt.show()

# Basic analysis
print("Resistance Distance Spectra:")
print("  Minimum value:", np.min(resistance_distance_spectrum))
print("  Maximum value:", np.max(resistance_distance_spectrum))
print("  Average value:", np.mean(resistance_distance_spectrum))

print("Distance Spectra:")
print("  Minimum value:", np.min(distance_spectrum))
print("  Maximum value:", np.max(distance_spectrum))
print("  Average value:", np.mean(distance_spectrum))

print("Signless Laplacian Spectra:")
print("  Minimum value:", np.min(signless_laplacian_spectrum))
print("  Maximum value:", np.max(signless_laplacian_spectrum))
print("  Average value:", np.mean(signless_laplacian_spectrum))

print("Normalized Laplacian Spectra:")
print("  Minimum value:", np.min(normalized_laplacian_spectrum))
print("  Maximum value:", np.max(normalized_laplacian_spectrum))
print("  Average value:", np.mean(normalized_laplacian_spectrum))

print("Adjacency Spectra:")
print("  Minimum value:", np.min(adjacency_spectrum))
print("  Maximum value:", np.max(adjacency_spectrum))
print("  Average value:", np.mean(adjacency_spectrum))
