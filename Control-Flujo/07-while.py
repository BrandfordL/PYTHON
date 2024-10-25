numero = 1 #Defino una variable
while numero < 100: #Evaluo si esto es verdadero para ejecutar lo que está dentro del bucle
    print(numero) #Me muestra el valor inicial de la variable
    numero *= 2 # Multiplica la variable x2

comando = "" #Defino una variable

while comando.lower() != "Salir": #Evalúo si esto es verdadero para ejecutar lo que está dentro del bucle
    comando = input("$ ") #Le preguntamos al usuario un comando a ingresar y se lo asignamos a la variable
    print(comando) #Imprimo el comando que el usuario ingresó
