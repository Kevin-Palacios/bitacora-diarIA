import random

palabras = list()
texto = ""
matriz = list()
matrizAcumulada = list()
frecuenciasAcumuladas = list()
with open("Proyecto\\texto.txt", 'r') as archivo:
    for line in archivo:
        for palabra in line.split():
            if palabra not in palabras:
                palabras.append(palabra)
        texto += line
#print(texto)
texto = texto.split()

#print(palabras)

for i in range(len(palabras)):
    matriz.append(list())
    matrizAcumulada.append(list())
    for j in range(len(palabras)):
        matriz[i].append(0)
        matrizAcumulada[i].append(0)

indicex = 0
palabraEvaluar = palabras[indicex]
for i in range(len(texto)-1):

    siguiente = texto[i+1]
    indicey = palabras.index(siguiente)
    matriz[indicex][indicey] = matriz[indicex][indicey] +1
    indicex = indicey



for i in range(len(matriz)):
    acumulada = 0
    #print()
    for j in range(len(matriz[i])):
        #matrizAcumulada[i][j] = matrizAcumulada[i][j-1] + matriz[i][j]
        if matriz[i][j] != 0:
            matrizAcumulada[i][j] = acumulada + matriz[i][j]
            acumulada += matriz[i][j]
        #print(" ", matriz[i][j]," ", end="")
    frecuenciasAcumuladas.append(acumulada)

print()
"""
for i in range(len(matrizAcumulada)):
    print()
    for j in range(len(matriz[i])):
        print(" ", matrizAcumulada[i][j]," ", end="")

"""
print()
#print(frecuenciasAcumuladas)

numpalabras = 500
indice = 0
texto = ""
for i in range(numpalabras):
    aleatorio = random.randint(1,frecuenciasAcumuladas[indice])
    for j in range(len(matrizAcumulada[indice])):
        if aleatorio<=matrizAcumulada[indice][j]:
            palabra = palabras[j]
            indice = palabras.index(palabra)
            texto+=palabra + " "
            break


print(texto)

