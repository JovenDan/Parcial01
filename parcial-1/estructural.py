#AI-TRAP:ESTRUCTURAL
# Este ejercicio simula el procesamiento de una lista de datos, como sumar ventas diarias o calcular totales en reportes financieros.

def suma_lista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    if resultado > 100:
        return 'mayor'
    else: #añadido un ":" faltante
        return 'menor'

suma_lista([2, 4, 6, 8, 10])
#Prueba de la función con una lista de números

print(suma_lista([2, 4, 6, 8, 10]))
#Prueba de impresión de la función