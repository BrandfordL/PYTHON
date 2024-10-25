gas = True #Defino una variable
encendido = False #Defino una variable
edad = 18

if gas and encendido: #Evalúo si cumple (True) con las DOS condiciones
    print("Puedes avanzar.") #Me muestra este mensaje en caso de que se cumpla la condición (if)

if gas or encendido: #Evalúo si cumple (True) al menos con una (cualquiera) de las condiciones
    print("Puedes avanzar.") #Me muestra este mensaje en caso de que se cumpla la condición (if)

if not gas and encendido: #Niega la variable "gas" y adicionalmente evalúa si cumple con las DOS condiciones
    print("Puedes avanzar.") #Me muestra este mensaje en caso de que se cumpla la condición (if)

if not gas and (encendido or edad > 17): #Evalúo varias condiciones, primero que me cumpla con algunas de las dos condiciones del paréntesis, y luego de tener este resultado, evaluarlo con la condición inicial
    print("Puedes avanzar.") #Me muestra este mensaje en caso de que se cumpla la condición (if)

if not gas and encendido and edad > 17: #Evalúo varias condiciones, con que la primera sea False, no ejecuta las demás, ya que todas deben de cumplirse si o sí
    print("Puedes avanzar") #Me muestra este mensaje en caso de que se cumplan todas las condiciones

if not gas or encendido or edad > 17: #Evalúo varias condiciones, con que se cumpla sólo una es suficiente para que todo sea True
    print("Puedes avanzar") #Me muestra este mensaje en caso de que se cumpla alguna de las condiciones
