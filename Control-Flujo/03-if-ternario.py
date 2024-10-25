edad = 15 #Defino la variable

if edad > 17: #Condición a evaluar con la variable
    mensaje = 'Es mayor.' #Si se cumple la condición (if) se almacenará éste mensaje en la variable
else:
    mensaje = 'Es menor.' #Si no se cumple la condición (if) se almacenará éste mensaje en la variable

print(mensaje) #Me muestra el mensaje que se almacenó en la variable "mensaje"

mensaje = "Es mayor." if edad > 17 else "Es menor." #Es otra forma de evaluar lo mismo anterior.
print(mensaje)
