x = input("Ingresa cualquier cosa: ")

print(int(x)) #Me muestra la variable x que ingrese convertida a número entero
print(str(x)) #Me muestra la variable x que ingrese convertida a cadena de texto (string)
print(float(x)) #Me muestra la variable x que ingrese convertida a decimal (float)
print(bool(x)) #Me muestra la variable x que ingrese convertida a boolean (Truue o False)

print(bool("")) #Me muestra la conversión del dato ingresado, es False ya que es una cadena vacía
print(bool("0")) #Me muestra la conversión del dato ingresado, es True ya que es una cadena con el caracter 0
print(bool(None)) #Me muestra la conversión del dato ingresado, es False ya que es el objeto None
print(bool(" ")) #Me muestra la conversión del dato ingresado, es True ya que es una cadena con el caracter de espacio ( )
print(bool(0)) #Me muestra la conversión del dato ingresado, es False ya que es 0
