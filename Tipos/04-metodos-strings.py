animal = " Brandford Feliz "
print(animal.upper()) #Me pasa todo el string a letras mayúsculas
print(animal.lower()) #Me pasa todo el string a letras minúsculas
print(animal.capitalize()) #Me pasa el primer caracter del string a letra mayúscula
print(animal.title()) #Me pasa el primer caracter de cada palabra del string a mayúscula
print(animal.strip()) #Quita los espacios de la izquierda y la derecha del string
print(animal.strip().capitalize()) #Inicialmente ejecuta el método strip y luego el capitalize
print(animal.lstrip()) #Quita los espacios de la izquierda del string
print(animal.rstrip()) #Quita los espacios de la derecha del string
print(animal.find("F")) #Busca el caracter indicado y devuelve el índice del mismo
print(animal.replace("ford", "forty")) #Busca los primeros caracteres indicados y los reemplaza por los segundos
print("Brand" in animal) #Busca los caracteres indicados y me indica por medio de un boolean (True, False) si se encuentran o no en la cadena
print("Brand" not in animal)#Busca los caracteres indicados y me indica por medio de un boolean (True, False) si NO se encuentran o no en la cadena
