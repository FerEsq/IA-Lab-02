'''
 * Autores:
    - Fernanda Esquivel - 21542
    - Adrian Fulladolsa - 21569
    - Elías Alvarado - 21808
 * Nombre: Ejercicio1_C.py
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 13.04.2024
    - Modificado el 13.04.2024
'''

import numpy as np
import matplotlib.pyplot as plt

def simulateDiceRolls(N):
    counts = []
    for _ in range(N):
        count = 1
        while True:
            roll = np.random.randint(1, 7)  #Simular un dado (1-6)
            if roll not in (1, 6):
                break
            count += 1
        counts.append(count)
    return counts

#Numero de simulaciones
Ns = [10, 100, 1000, 10000]

#Diccionario para guardar los resultados
results = {}

#Realizar simulaciones
for N in Ns:
    results[N] = simulateDiceRolls(N)

#Graficar los resultados
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, N in enumerate(Ns):
    axes[i].hist(results[N], bins=range(1, max(results[N]) + 2), align='left', density=True, rwidth=0.8)
    axes[i].set_title(f'N = {N}')
    axes[i].set_xlabel('Number of Rolls')
    axes[i].set_ylabel('Probability')
    axes[i].grid(True)

plt.tight_layout()
plt.show()
