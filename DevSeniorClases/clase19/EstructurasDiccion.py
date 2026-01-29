usuarios = {
    "u001": {"nombre": "Ana", "correo": "ana@mail.com", "roles": ["admin"]},
    "u002": {"nombre": "Pedro", "correo": "pedro@mail.com", "roles": ["cliente"]}
}

#Acceder al nombre del usuario "u001"
usuario = "u00"
print("Nombre del usuario u001:", usuarios['u001']['nombre'])

#Agregar un nuevo rol al usuario "u002"
usuarios['u002']['roles'].append('ventas')
print("Roles actualizados del usuario u002:", usuarios['u002']['roles'])

#Agregar un nuevo usuario 
usuarios ['u003']= {"nombre": "Santiago", "correo": "santi@mail.com", "roles": [""]}
usuarios ['u004']= {"nombre": "Juan", "correo": "jua@mail.com", "roles": ["secretario"]}

print("\nListado de usuarios registrados: ")
for id_usuario, valores_usuario in usuarios.items():
    print(f"{id_usuario} - {valores_usuario}")
    
#  Buscar un usuario de acuerdo  a su rol 
rol = " secretario "
print(f"\nBuscar el rol {rol}")
for id_usuario,valores_usuario in usuarios.items():
    if rol in valores_usuario.get("roles", []):
        print(f"Usuario: {id_usuario} - nombre: {valores_usuario['nombre']}")