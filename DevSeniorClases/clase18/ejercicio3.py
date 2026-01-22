#slice

ventas_mensuales = [12000, 9800, 10200, 14500, 16000, 13200, 11000, 11700, 9800, 10500, 14000, 13800]

for venta in enumerate(ventas_mensuales,start=1):
    print(venta)
    
ventas_T2 =  ventas_mensuales[3:6]

ventas_top = [v for v in ventas_mensuales if v > 13000]

print(f"Ventas del segundo trimestre {ventas_T2}")
print(f"Ventas Top {ventas_top}")
