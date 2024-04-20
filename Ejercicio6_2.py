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
import matplotlib.pyplot as plt
import random


p = 0.3
G = nx.DiGraph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('D', 'H'),
    ('H', 'J'), ('E', 'J'), ('E', 'I'), ('E', 'F'), ('I', 'G'), ('F', 'G')
]
G.add_edges_from(edges)

def simulate_walk_no_return(graph, start, end, block_prob):
    path = [start]
    current = start
    
    while current != end:
        neighbors = list(graph.neighbors(current))
        forward_neighbors = [node for node in neighbors if node >= current]

        open_neighbors = [node for node in forward_neighbors if random.random() > block_prob]
        
        if not open_neighbors:
            return None
        else:
            next_node = random.choice(open_neighbors)
        
        path.append(next_node)
        current = next_node
    
    return path

pasos_a_j=[]
for _ in range(0,10000):
    pasos = simulate_walk_no_return(G, 'A', 'J', p)
    if pasos != None:
        pasos_a_j.append(len(pasos))


plt.figure(figsize=(10, 5))
plt.hist(pasos_a_j, bins=range(1, max(pasos_a_j) + 2), align='left', color='blue', rwidth=0.8)
plt.title('Distribución del número de pasos hasta llegar a J')
plt.xlabel('Número de pasos')
plt.ylabel('Frecuencia')
plt.xticks(range(1, max(pasos_a_j) + 1))
plt.grid(True)
plt.show()