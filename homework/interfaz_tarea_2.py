'''
Variables a considerar:
- (int) opcion: itera por las diferentes opciones que el usuario puede escoger [1¦2¦9¦0]
- (int) numBitsMantisa: numero de bits para la mantisa
- (int) numBitsExponente: numero de bits para el exponente
'''
from tarea2 import Bmachine

def inicio():
    opcion = 0
    while (True):
            #creacion de la maquina
            if (opcion == 0):
                print("Ingrese el numero de bits destinados a la mantisa: ")
                try:
                    #numero de bits para la mantisa
                    numBitsMantisa = int(input())
                except ValueError as e:
                    if type(numBitsMantisa) != type(1):
                        print('\nError: Porfavor ingrese un numero entero de bits.')
                        return 0
                if (numBitsMantisa <= 0):
                    print("Error: No se puede crear un maquina con una mantisa de esta cantidad de bits")
                    return 0
                    
                print("Ingrese el numero de bits destinados al exponente: ")
                try:
                    #numero de bits para el exponente
                    numBitsExponente = int(input())
                except ValueError as e:
                    if type(numBitsExponente) != type(1):
                        print('\nError: Porfavor ingrese un numero entero de bits.')
                        return 0
                if (numBitsExponente <= 0):
                    print("Error: No se puede crear un maquina con un exponente de esta cantidad de bits")
                    return 0

                if ((numBitsExponente + numBitsMantisa + 2) < 8):
                    print("Error: Recuerda que la maquina debe ser por lo minimo de 8 bits.")
                    return 0

                #informacion sobre la maquina creada
                print("\n\n\nFelicitaciones! Has construido una maquina de", (numBitsExponente + numBitsMantisa + 2), "bits.")
                print("- Usa 1 bit para el signo de la mantisa, 1 bit para el signo del exponente.")
                print("- ", numBitsExponente," bit(s) para el exponente")
                print("- ", numBitsMantisa, " bit(s) para la mantisa (respectivamente).")
                
                bm = Bmachine(int(numBitsExponente + numBitsMantisa + 2), int(numBitsMantisa), int(numBitsExponente))

                #datos de interes(numero mas gande - epsilon)
                print("\n\nAqui algunos datos interesantes de la maquina que creaste !","\U0001F603", \
                        "\nEpsilon de la maquina: ", bm.eps, \
                        "\nNumero mas grande que tu maquina soporta: ", bm.max_num)

            #opciones
            print('\nOpciones:\n                   1. Para converitr de numero decimal -> numero maquina.\n \
                  2. Para convertir de numero maquina -> numero decimal.\n \
                  9. Para salir del programa.\n \
                  0. Para cambiar de maquina.')
            print("Ingresa una de las opciones [1,2,9,0]:")
            opcion = int(input())

            #convertir numero decimal -> maquina
            if (opcion == 1):
                print("Ingrese el numero decimal a convertir a maquina. (Use por favor el punto como separador decimal.)")
                num = input()
                if ',' in str(num):
                    num = num.replace(',', '.')

                else:
                    if '.' not in str(num):
                        num = "%s.0" % (str(num))

                numbers = str(num).split('.')
                units = int(numbers[0])
                decimal = int(numbers[1])

                print("Numero Maquina: ", bm.dec_to_machine(units, decimal))

            #convertir numero maquina -> decimal
            if (opcion == 2):
                print("Ingrese el numero maquina a convertir a decimal. (Siguiendo la estructura de la maquina.)")

                a = input()
                str(a)
                if ('2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a):
                    print("Error: Porfavor solo ingresa cero (0) o uno (1).")

                # FALTA HACER CHEQUEO POR INPUT ERRONEO
                print("Numero Decimal: ", bm.machine_to_dec(input()))

            #salir del programa
            if(opcion == 9):
                print('\n\n\nChao ¯\_(ツ)_/¯',)
                return

inicio()
