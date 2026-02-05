mi_set = set()
frutas = {"pera", "manzana" , "banano"}

# conversion de lista a set

numeros = [1,2,3,4]
conversion = set(numeros)
print(conversion)

frutas = {"pera", "manzana" , "banano"}
frutas.add("uva")
print(frutas)

frutas.update(["kiwi", "mango"])
print(frutas)

frutas.discard("pera")# si el elemento no existe da error al borrar
print(frutas)

#frutas.remove("pera") #Aqui si da error porque el elemento no existe 
frutas = sorted(frutas)
frutas.clear()
print(frutas)

#Operaciones con set
#union 
#interseccion
#diferencia
#diferencia simetrica

a = {1,2,3}
b = {3,4,5}
#union 
print(a|b)# {1,2,3,4,5}
#interseccion
print(a & b) #{3}
#diferencia
print(a - b)#{1,2}
#diferencia simetrica
print(a ^ b) # {1,2,4,5}

#validacion de elmentos con set

usuario = {"Maryam", "Pablo","Ignacio"}
print("Maryam" in usuario) #True o False
print("Luis" in usuario)


