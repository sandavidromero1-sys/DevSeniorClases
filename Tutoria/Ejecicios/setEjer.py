nombre1 = {"Juan","Ana","Pedro","Pablo"}
nombre2 = {"Laura","Janeth","Kamila","Ana"}

nombres = nombre1.union(nombre2)
print(nombres)

nomInrse= nombre1.intersection(nombre2)
print(nomInrse)

nombresDif = nombre1.difference(nombre2)
print(nombresDif)

nombresDif2 = nombre2.difference(nombre1)
print(nombresDif2)

print(len(nombre1))


