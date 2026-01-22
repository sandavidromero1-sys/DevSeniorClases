# lista = []
# lista.append("Manzana")
# print(lista)

# lista2 = ["fabian","cesar",22]

# lista3 = [lista2,"manzana",10,3.1416,True,lista2]
# print(lista3)
# lista3.pop(2)
# print(lista3)
# lista3.remove(lista2)

# for i in range (len(lista3)):
#     if lista3[i] == 10:
#         lista3.remove(i)
        
# print(lista3)

# borrar = ["manzana", True]
# lista4 = [item for item in lista3 if item not in borrar]
# print(lista4)



# lista5 = [2,3,4,5,8.214,1.618,7]
# lista5.sort()
# print(lista5)
# lista5.reverse()
# print(lista5)
# lista5.clear()
# print(lista5)

lista_precios = [50,75,46,28,80,65,8]
lista_precios.sort()
print(lista_precios)

def mostrar_mayor():
    for i in range(len(lista_precios)):
        if lista_precios[i] == max(lista_precios):
            print(f"el mayor es: {lista_precios[i]}")
def mostrar_menor():
    for i in range(len(lista_precios)):
        if lista_precios[i] == min(lista_precios):
            print(f"el menor es: {lista_precios[i]}")
            
mostrar_mayor()
mostrar_menor()
    