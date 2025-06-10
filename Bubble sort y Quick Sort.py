import time
# Ordenamiento por burbuja según prioridad (Bubble Sort)
def bubble_sort(productos):
    n = len(productos) 
    for i in range(n - 1):
        intercambio_realizado = False
        for x in range(n - 1 - i):
            # Compara la prioridad (primer elemento de la sublista)
            if productos[x][0] > productos[x + 1][0]:
                productos[x], productos[x + 1] = productos[x + 1], productos[x] 
                intercambio_realizado = True
        if not intercambio_realizado:
            break
    return productos

# Ordenamiento rápido según prioridad (Quick Sort)
def quick_sort(productos):
    if len(productos) <= 1:
        return productos
    else:
        pivote = productos[0]
        menores = [x for x in productos[1:] if x[0] <= pivote[0]]
        mayores = [x for x in productos[1:] if x[0] > pivote[0]]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

productos = [[5, "Manteca"], [6, "Fiambre"], [2, "Fideos"], [1, "Leche"], [3, "Arroz"], [4, "Pan"]]


ordenados_burbuja = bubble_sort(productos)
ordenados_rapido  = quick_sort(productos)

#Bubble Sort
print("Lista Bubble Sort segun prioridad:") 
for producto in ordenados_burbuja:
    print(f"{producto[0]}: {producto[1]}")

# Quick Sort
print("\nLista Quick Sort segun prioridad:") 
ordenados_rapido = quick_sort(productos.copy())
for prioridad, nombre in ordenados_rapido:
    print(f"{prioridad}: {nombre}")

print("\n--- Prueba con lista de ejemplo original (N=6) ---")

# Comparación de tiempos
# Bubble Sort
productos_burbuja = productos.copy()
inicio_bubble = time.time()
bubble_sort(productos_burbuja)
fin_bubble = time.time()
tiempo_bubble = fin_bubble - inicio_bubble

# Quick Sort
productos_quick = productos.copy()
inicio_quick = time.time()
quick_sort(productos_quick)
fin_quick = time.time()
tiempo_quick = fin_quick - inicio_quick

# Resultados
print(f"Tiempo Bubble Sort: {tiempo_bubble:.6f} segundos")
print(f"Tiempo Quick Sort : {tiempo_quick:.6f} segundos")