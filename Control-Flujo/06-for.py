for numero in range(5): #El bucle itera 5 veces, cada vez le va a asignar un valor distinto a numero, en este caso el rango de 0 a 5 que incluye 5 iteraciones.
    print(numero, numero * 'Hola mundo ') #Me muestra todos los valores del range que se guardaron en la variable numero, y ademas multiplico cada valor por 'Hola mundo'

buscar = 10 #Definimos una variable
for numero in range(5): #Utilizo un bucle para recorrer todos los valores de range e irle asignando un valor a la variable numero
    print(numero) #Me muestra los valores que se van asignandole a la variable numero.
    if numero == buscar: #Una condición la cual nos permite encontrar cuando el valor de numero sea igual al valor de la variable buscar.
        print("Econtrado, ", buscar) #Me muestra este mensaje cuando se cumpla la condicion y ademas me mostrara el valor de la variable buscar.
        break #Nos permite detener la ejecución del script una vez se haya encontrado el valor buscado.
else: #Se ejecutará esta condicional en caso de que no se cumpla el if, es decir, el numero a buscar no se encuentre dentro del range
    print("No encontré el número buscado") #Me mostrara este mensaje como ejecución del else

for char in "Ultimate Python": #Utilizo un bucle con la iteración char para buscar cada caracter de la cadena indicada
    print(char) #Imprimo cada caracter de la cadena
