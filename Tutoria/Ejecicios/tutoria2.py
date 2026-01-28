lista_original= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def trasponer_matriz(lista_original):
    n = len(lista_original)
    
    matriz_traspuesta = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
           
            matriz_traspuesta[j][i] = lista_original[i][j]
            
    return matriz_traspuesta


matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = trasponer_matriz(matriz_ejemplo)
print(resultado)
    