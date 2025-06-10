import random
import time

# Generador de productos aleatorios
def generar_productos(cantidad):
    productos = []
    nombres_ejemplo = ["Leche", "Pan", "Fideos", "Arroz", "Manteca", "Fiambre", "Jugo", "Cereal", "Frutas", "Verduras"]
    for _ in range(cantidad):
        prioridad = random.randint(1, 1000)
        nombre = random.choice(nombres_ejemplo)
        productos.append([prioridad, nombre])
    return productos

# Ordenamiento por burbuja según prioridad (Bubble Sort)
def bubble_sort(lista):
    n = len(lista) 
    for i in range(n - 1):
        intercambio_realizado = False
        for x in range(n - 1 - i):
            # Compara la prioridad (primer elemento de la sublista)
            if lista[x][0] > lista [x + 1][0]:
                lista[x], lista[x + 1] = lista[x + 1], lista[x] 
                intercambio_realizado = True
        if not intercambio_realizado:
            break
    return lista

# Ordenamiento rápido según prioridad (Quick Sort)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[0] <= pivote[0]]
        mayores = [x for x in lista[1:] if x[0] > pivote[0]]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)


# Generar lista de productos
cantidad_productos = 5000  # Puedes aumentar o reducir este número para comparar
productos = generar_productos(cantidad_productos)

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
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Tiempo Bubble Sort: {tiempo_bubble:.6f} segundos")
print(f"Tiempo Quick Sort : {tiempo_quick:.6f} segundos")
