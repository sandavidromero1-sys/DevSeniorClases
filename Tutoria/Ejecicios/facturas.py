def generar_factura():
  factura_id=input("numero de la factura: ")
  cliente=input("nombre del cliente: ")
  productos=[]
  total=0
  
  while True:
    prod= input("producto(o 'fin' para terminar): ")
      
    if prod.lower()=='fin':
        break
    cant=int(input("cantidad: "))
    precio=float(input("precio unitario: "))
    subtotal=cant*precio
    productos.append(f"{prod} x {cant} -$ {subtotal:.2f}")
    total += subtotal
      
    with open(f"factura_{factura_id}.txt", "w") as archivo:
        archivo.write(f"Factura ID: {factura_id}\n")
        archivo.write(f"Cliente: {cliente}\n")
        archivo.write("_"*20 + "\n")
        for item in productos:
            archivo.write(item + "\n") 
        archivo.write("_"*20 + "\n")
        archivo.write(f"Total: $ {total:.2f}\n")
  print(f"Factura {factura_id} generada exitosamente.")
  
def main():
    generar_factura()
    
if __name__ == "__main__":
    main()
