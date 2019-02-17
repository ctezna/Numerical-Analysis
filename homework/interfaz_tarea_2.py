'''
Variables a considerar:

- (int) opcion: itera por las diferentes opciones que el usuario puede escoger [1¦2¦9¦0]
- (int) numBits: bits totales de la maquina
- (int) numBitsMantisa: numero de bits para la mantisa
- (int) numBitsExponente: numero de bits para el exponente

'''

def inicio():
    opcion = 0
    while (True):
            #creacion de la maquina
            if (opcion == 0):
                print("Ingrese el numero de bits que tendra su maquina: ")
                try:
                    #bits totales de la maquina
                    numBits = int(input())
                except ValueError as e:
                    if type(numBits) != type(1):
                            print('\nError: Porfavor ingrese un numero entero de bits.')
                            return 0

                print("Ingrese el numero de bits destinados a la mantisa: ")
                try:
                    #numero de bits para la mantisa
                    numBitsMantisa = int(input())
                except ValueError as e:
                    if type(numBits) != type(1):
                            print('\nError: Porfavor ingrese un numero entero de bits.')
                            return 0

                print("Ingrese el numero de bits destinados al exponente: ")
                try:
                    #numero de bits para el exponente
                    numBitsExponente = int(input())
                except ValueError as e:
                    if type(numBits) != type(1):
                            print('\nError: Porfavor ingrese un numero entero de bits.')
                            return 0

                if numBitsExponente+numBitsMantisa+2 > numBits:
                    print('\nError: La maquina no soporta la cantidad de bits ingresados mantisa/exponente.\n(Recuerda que tienes que ingresar 2 bits menos que el numero total de bits).')
                    return 0

                if numBits != 2+(numBitsExponente+numBitsMantisa):
                    print('\nError: El numero de bits de la mantisa/exponente no coincide con el numero total de bits de la maquina.')
                    return 0        

                #informacion sobre la maquina creada
                print("\n\n\nFelicitaciones! Has construido una maquina de", numBits, "bits, que usa 1 bit para el signo de la mantisa, 1 bit para el signo del exponente,", numBitsExponente,\
                    "bit(s) para el exponente y", numBitsMantisa, "bit(s) para la mantisa (respectivamente).")

                #datos de interes(numero mas gande - epsilon)
                print("\n\nAqui algunos datos interesantes de la mauqina que creaste !","\U0001F603", \
                        "\nEpsilon de la maquina: " , 'varEpsilon?', \
                        "\nNumero mas grande que tu maquina soporta: ", 'varMas_Grande')

            #opciones
            print('\nOpciones:\n                   1. Para converitr de numero decimal -> numero maquina.\n \
                  2. Para convertir de numero maquina -> numero decimal.\n \
                  9. Para salir del programa.\n \
                  0. Para cambiar de maquina.')
            print("Ingresa una de las opciones [1,2,9,0]:")
            opcion = int(input())

            #convertir numero decimal -> maquina
            if (opcion == 1):
                #codigo
                print("resultado maquina")

            #convertir numero maquina -> decimal
            if (opcion == 2):
                #codigo
                print("resultado decimal")

            #salir del programa
            if(opcion == 9):
                print('\n\n\nChao ¯\_(ツ)_/¯',)
                return

inicio()
