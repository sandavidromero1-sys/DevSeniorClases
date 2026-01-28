#cree una tupla con diferentes tipos de datos e imprima la misma utilice una función para la impresión

Datos = ("perro",12,123.1223,"Juan")

def imprimir() :

    for i in range(len(Datos)):
        print( f"-Dato {i}: {Datos[i]}")
        
imprimir()
    