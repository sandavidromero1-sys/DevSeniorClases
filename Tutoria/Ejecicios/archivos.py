# with open ("archivo.txt", "w", encoding="utf-8") as file:
#     file.write("Hola, este es un archivo de texto.\n")
#     file.write("Estamos aprendiendo a manejar archivos en Python.\n")

# with open ("archivo.txt", "a", encoding="utf-8") as file:
#     file.write("\nEsta es una línea adicional.")

# with open ("archivo.txt", "r", encoding="utf-8") as file:
#     contenio = file.read()
#     print(contenio)

#Ejercicio 
# with open ("ejercicio.txt","w", encoding="utf-8") as f:
#     f.write("Ejercicio de archivos")
#     f.write("\nManejo de archivos en python")

# with open ("ejercicio.txt","a", encoding="utf-8") as f:
#     f.write("\namigo")

# with open ("ejercicio.txt","r", encoding="utf-8") as f:
#     contenido = f.read()
#     print(contenido)
    
with open ("ejercicio.txt","r") as file:
    lines = file.readlines()
with open ("ejercicio.txt", "w")as file:
    for line in lines:
        if line.strip() != "Manejo de archivos en pythonLinea adicional":
            file.write(line)
with open ("ejercicio.txt","r") as file:
    contenido = file.read()
    print(contenido)
    

with open ("ejercicio.txt","r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)
   
    
    
