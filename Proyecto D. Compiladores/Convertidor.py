



from decimal import HAVE_CONTEXTVAR
from typing import BinaryIO

#DECIMAL A HEXADECIMA
def obtener_caracter_hexadecimal(valor):

    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def decimal_a_hexadecimal(numero):
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        numero = int(numero / 16)
    return hexadecimal
#DECIMAL A OCTAL
def decimal_a_octal(numero):
    octal = ""
    while numero > 0:
       residuo = numero % 8
       octal = str(residuo)+ octal
       numero = int(numero//8)
    return octal
#DECIMAL A BINARIO
def decimal_a_binario(numero):
    if numero < 0:
        return "0"
    binario = ""
    while numero > 0:
        residuo = int(numero)%2
        numero = int(numero/2)
        binario = str(residuo) + binario
    return binario
#DECIMAL A ROMANOS
def decimal_a_romano(numero):
    decimal = int(numero)
    lis_dec = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    lis_rom = [ 'M', 'CM','D', 'CD', 'C','XC','L','XL','X','IX','V','IV','I']
    res = ""
    i = 0
    while decimal>0:
        for x in range(decimal//lis_dec[i]):
            res = res + lis_rom[i]
            decimal = decimal - lis_dec [i] 
        i+= 1
    return res


