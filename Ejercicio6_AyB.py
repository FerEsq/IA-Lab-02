'''
 * Autores:
    - Fernanda Esquivel - 21542
    - Adrian Fulladolsa - 21569
    - Elías Alvarado - 21808
 * Nombre: Ejercicio6_1.py
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 13.04.2024
    - Modificado el 13.04.2024
'''
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt


p = 0.2
G = nx.DiGraph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('D', 'H'),
    ('H', 'J'), ('E', 'J'), ('E', 'I'), ('E', 'F'), ('I', 'G'), ('F', 'G')
]
G.add_edges_from(edges)

def simulate_walk_fixed_steps(graph, start, end, block_prob, max_steps):
    path = [start]
    current = start
    steps = 0
    steps_to_J = 0
    J_found = False
    
    for _ in range(max_steps):
        if current == end:
            break
        
        neighbors = list(graph.neighbors(current))
        forward_neighbors = [node for node in neighbors if node >= current]
        open_neighbors = [node for node in forward_neighbors if random.random() > block_prob]
        
        if not open_neighbors:
            break
        else:
            next_node = random.choice(open_neighbors)
            path.append(next_node)
            current = next_node
            steps += 1
            if not J_found and current == end:
                steps_to_J = steps
                J_found = True
            
    
    return steps_to_J, current,path

N = 10000  
M = 15    

steps_to_J = []
final_positions = {}

for _ in range(N):
    steps, final_node, path = simulate_walk_fixed_steps(G, 'A', 'J', p, M)
    steps_to_J.append(steps)
    if final_node in final_positions:
        final_positions[final_node] += 1
    else:
        final_positions[final_node] = 1



plt.figure(figsize=(10, 5))
plt.hist(steps_to_J, bins=range(1, max(steps_to_J) + 2), align='left', color='blue', rwidth=0.8)
plt.title('Distribución del número de pasos hasta llegar a J')
plt.xlabel('Número de pasos')
plt.ylabel('Frecuencia')
plt.xticks(range(1, max(steps_to_J) + 1))
plt.grid(True)
plt.show()

# Crear el gráfico de barras para la distribución de posiciones después de M movimientos
plt.figure(figsize=(12, 6))
nodes = list(final_positions.keys())
frequencies = [final_positions[node] for node in nodes]
plt.bar(nodes, frequencies, color='green')
plt.title('Distribución de posiciones en los nodos después de 15 movimientos')
plt.xlabel('Nodos')
plt.ylabel('Frecuencia de visitas')
plt.grid(True)
plt.show()
