edad = 70 #Defino la variable con la que trabajaremos el if
if 17 < edad < 54: #Esta es la condición que debe de cumplir para poder ejecutar la siguiente líne a de código
    print("Puede ver la película.") #Me muestra este mensaje en caso de cumplir el if
elif 65 > edad > 54:
    print("Puede ver la película con descuento.") #Me muestra este mensaje en caso de no cumplir el if y si el elif
elif edad > 65:
    print("Puede ver la película con super descuento.") #Me muestra este mensaje en caso de no cumplir ninguna de las condiciones anteriores (if, elif), y sí éste elif
else:
    print("No puede ver la película.") #Me muestra este mensaje en caso de NO cumplir ninguna de las condiciones anteriores

print("Listo") #Me muestra este mensaje para terminación del programa
