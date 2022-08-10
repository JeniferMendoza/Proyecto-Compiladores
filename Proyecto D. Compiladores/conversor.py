
import Convertidor

def solictar_datos():
     bases_soportadas = ["2", "8", "16", "4", ]
     
     base_destino = input("""
       2 - Binario
       8 - Octal
       16 - Hexadecimal
       4  - Romano
       Elige la base a la que conviertes: [2, 8, 16, 4]: """)
      
     if base_destino not in bases_soportadas:
        print("La base destino no esta soportada")
        return 
     numero = int(input("Ingresa el número a convertir: "))
     return(convertir( base_destino , numero))

def convertir( base_destino , numero):
    if base_destino == "2":
        return Convertidor.decimal_a_binario(numero)
    elif base_destino == "8":
        return Convertidor.decimal_a_octal(numero)
    elif base_destino == "16":
        return Convertidor.decimal_a_hexadecimal(numero)
    elif base_destino == "4":
        return Convertidor.decimal_a_romano(numero) 

print(solictar_datos())



