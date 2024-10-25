n1 = input("Ingresa el perimer número: ") #Permite al usuario ingresar el primer número
n2 = input("Ingresa el segundo número: ") #Permite al usuario ingresar el segundo número

n1 = int(n1) #Defino las variables ingresadas como enteros
n2 = int(n2) #Defino las variables ingresadas como enteros

#Realiza cada operación y el resultado lo almacena en cada variable definida
suma = n1 + n2
res = n1 - n2
mul = n1 * n2
div = n1 / n2

#Define la cadena de texto que me mostrará los resultados de las operaciones
mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma},
el resultado de la resta es {res},
el resultado de la multiplicación es {mul},
el resultado de la división es {div},
"""
print(mensaje) #Muestra la cadena de texto con los resultados de las operaciones
