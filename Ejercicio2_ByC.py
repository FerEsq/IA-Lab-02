'''
 * Autores:
    - Fernanda Esquivel - 21542
    - Adrian Fulladolsa - 21569
    - Elías Alvarado - 21808
 * Nombre: Ejercici21_ByC.py
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 13.04.2024
    - Modificado el 13.04.2024
'''
import numpy as np
import matplotlib.pyplot as plt

def simular_lanzamientos(N = None):
    if N == None:
        N = int(input("Ingrese la cantidad N de veces que se simulara el lanzamiento de los dados "))
    resultados = []
    for i in range(0, N):
        D1 = np.random.randint(1, 7)
        D2 = np.random.randint(1, 7)
        resultados.append(D1+D2)
    promedio = 0
    for res in resultados:
        promedio += res
    promedio = promedio//N
    print("El resultado promedio obtenido es de",promedio," para ",N," veces")
    return promedio
    
    
def graficar_frecuencias(m,data):
    valores, frecuencias = np.unique(data, return_counts=True)
    title = 'Distribucion de promedios para un total de '+str(m)+' veces'
    plt.figure(figsize=(10, 6))
    plt.bar(valores, frecuencias, color='blue') 
    plt.xlabel('Promedios')
    plt.ylabel('Frecuencia')
    plt.title(title)
    plt.xticks(valores)
    plt.grid(True) 
    plt.show()

while True:
    option = int(input("Cual inciso? \n1. Inciso B\n2. Inciso C\n"))
    if option == 1:
        simular_lanzamientos()
    elif option == 2:
        arr = [5,10,50,100,200]
        for m in arr:
            promedios = []
            for i in range(0,m):
                promedios.append(simular_lanzamientos(10))
            graficar_frecuencias(m,promedios)
    else:
        exit(0)