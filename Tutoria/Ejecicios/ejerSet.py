#Eliminar los sensores defectusos

sensores = {"sensor1","sensor2","sensor3","sensor4"}
defectusos = {"sensor1","sensor3"}

elimDef = sensores.difference(defectusos)
print(f"Los sensores disponibles son:\n{elimDef}")