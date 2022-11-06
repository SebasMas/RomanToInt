
#Tenemos un diccionario que representa la equivalencia de un número Romano a un número entero
romanos = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#Asignamos un variable "Valor" que es el número romano que vamos a ingresar, este número romano está asignado como "Str" por lo tanto solo usamos "Input()" y no "int(input())"

variable = int(input("¿Cuántos números va a ingresar?: "))


#Si variable es mayor que 1, entonces proceda preguntando cada numero que va a ingresar "variable" veces
if variable>1:
    #Añadimos una pequeña lista para que cada número que ingresemos se guarde ahí
    lista = []
    for n in range(variable):
        num = input("Ingrese un número en romano: ")
        lista.append(num)
    #Una vez tengamos todos los números romanos en esta lista, lo siguiente es que por cada numero de esa lista, python lo cambie por un entero equivalente al "num" que se ingresó   
    enteros = []
    for num in lista:
        int = romanos[num]
        enteros.append(int)
        #Al tener ya todos los valores equivalentes de los romanos en enteros, ya solo tenemos que sumar todos los valores de esa lista
        resultado = sum(enteros)
        print(resultado)
    

elif variable<2:
    
    valor = input("Ingrese un número en romano: ")
    #Por cada romano en el diccionario romanos
    for romano  in romanos:
        #La variable "int" (entero) va a ser igual a el "valor", que está asignado como "str", en la lista romanos
        int = romanos[valor]
        
    print(int)
    
    