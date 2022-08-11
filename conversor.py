from decimal import HAVE_CONTEXTVAR
from typing import BinaryIO
import random
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

#ALTERNATIVO
def alternativo(a):
    simb0 = "Ჶ"
    simb1 = "•"
    simb5 = "ꟷꟷꟷꟷ"
    b = a
    c = 1
    cont = 1
    f = []
    d = 1
    k = 0

    while c>=1:
        b = b/20
        if b>1:
            cont += 1
        elif b==1:
            cont += 1
        else:
            c = 0
    b=a
    while cont!=0:
        d=1
        if cont==1:
            d=1
        else:
            for i in range(cont-1):
                d=d*20

        e=b%d
        f.append(int((b-e)/d))
        b=e
        c+=1
        cont-=1

    for i in range(c):
        print("= = = = = =")
        g = 0
        num = f[k]
        if num == 0:
            print("=         =")
            print("=    "+simb0+"    =")

        h=0
        while num != 0:
            if num > 4:
                e=num%5
                g = int((num-e)/5)
                num=e
                if num==0:
                    print("=         =")
            else:
                h=1
                if g < 3:
                    print("=         =")
                print("=  ", end="")
                if num == 3 or num == 2:
                    print(" ", end="")
                elif num == 1:
                    print("  ", end="")
                for i in range(num):
                    print(simb1, end="")
                if num == 2 or num == 1:
                    print("    =")
                else:
                    print("   =")
                num=0

        for i in range(g):
            print("=  "+simb5+"   =")
        if (g == 1 and h == 1) or (g == 2 and h == 0):
            print("=         =")
        elif g == 1 and h == 0:
            print("=         =")
            print("=         =")
        elif g == 0:
            print("=         =")
            print("=         =")

        print("= = = = = =")
        k+=1

#ALEATORIO
def aleatorio(decimal):
    res=""
    num =  random.randint(1,5)
    if num == 1:
        res=decimal_a_hexadecimal(decimal)
        return res
    elif num == 2:
        res=decimal_a_octal(decimal)
        return res
    elif num == 3:
        res=decimal_a_binario(decimal)
        return res
    elif num == 4:
        res=decimal_a_romano(decimal)
        return res
    elif num == 5:
        alternativo(decimal)
        return 'maya'


