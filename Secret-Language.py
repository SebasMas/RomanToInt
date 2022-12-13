abecedario = {"a" : 1 , "b" : 2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "ñ":15, "o":16, "p":17, "q":18, "r":19, "s":20, "t":21, "u":22, "v":23, "w":24, "x":25, "y":26, "z":27}



continuar = True
while continuar:
    opcion = int(input("LEER (1) - CONVERTIR (2): "))
    
    if opcion == 1:
        cantidad = int(input("Cuántos números son?: "))

        list = []
        for n in range(cantidad):
            entero = int(input("Ingrese el número: "))
            for n in abecedario:
                texto = abecedario[entero]
            list.append(texto) 
        print(list)
        
    

    elif opcion == 2:
        cantidad = int(input("Cuántas letras tiene su frase?: "))

        list = []
        for n in range(cantidad):
            texto = input("Ingrese la letra: ") 
            for letra in abecedario:
                entero = abecedario[texto]
            list.append(entero) 
        print(list)
 