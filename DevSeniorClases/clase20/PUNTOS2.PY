"""
Ejercicio 2 — Verificar acceso (operador in)
Un sistema tiene usuarios autorizados:
usuarios_autorizados = {"ana", "carlos", "maria", "pedro"}
El programa debe pedir un nombre y decir si puede entrar o no.
Actividad
•	Solicitar un nombre con input
•	Indicar si pertenece al conjunto
Qué debe aprender el estudiante: Los sets permiten búsquedas extremadamente rápidas (mejor que lista)
# """
 
def verficar_usuario (perfil,usuarios)-> str:
    
    for  u in usuarios: 
        if u == perfil:
            return (f"!!!!Validacion Exitosa!!!!\n Puede ingresar {perfil}")
    return (f"Acceso Denegado, vuelva a intentarlo {perfil}") 

def main() -> None:

    usuarios = {"ana", "carlos", "maria", "pedro"}
    
    
    perfil = input(str("Ingrese su primer nombre: "))

    resultado = verficar_usuario(perfil,usuarios)
    print(resultado)
    
if __name__ == "__main__":
     main()