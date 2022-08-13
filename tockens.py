import re
from traceback import print_list
import conversor
#from Asintactico import ASintaxis

ErrorLines=[]
def ASintaxis():
    #Expresion='[\d+]([A-Z]|[a-z])+$'
    Exp=re.compile('^\d+\s+\w+\s+\$\n*$')
    texto=open("instrucciones.txt")
    tlines=texto.readlines()
    i=0
    error=[]
    resultado=[]
    while(i<len(tlines)):
        text=tlines[i]
        i+=1
        if Exp.match(text) is not None:
            resultado.append(f'{i}: '+str(LinesToken[i-1]))
        else:
            ErrorLines.append(i)
            error.append(f"{i}: Error de sintaxis en la linea {i}")
    MostrarResultados()

def MostrarResultados():
    print('Resultados: \n')
    HacerConversiones()
    print('\n')
    print(f'TOKENS Encotrados: {NToken}')
    for i in LinesToken:
        a=0
        while(a<len(i)):
            print(i[a])
            a+=1
    

def HacerConversiones():
    l=0
    Salidas=[]
    while(l<len(tlines)):
        text=tlines[l]
        #Salidas=[]
        l+=1
        if(l in ErrorLines):
            #Salidas.append(f'{l}: Error')
            print(f'{l}: Error. Errore de Sintaxis en la linea {l}')
        else:
            if re.search(t_digitos,text) is not None:
                text2 = re.search(t_digitos,text)
                decimal = int(text2[0])
                if re.search(t_hexadecimal,text) is not None:
                    #Salidas.append(f'{l} Hexadecimal: {conversor.decimal_a_hexadecimal(decimal)}')
                    print((f'{l} Hexadecimal: {conversor.decimal_a_hexadecimal(decimal)}'))
                elif re.search(t_octal,text) is not None:
                    #Salidas.append(f'{l} Octal: {conversor.decimal_a_octal(decimal)}')
                    print((f'{l} Octal: {conversor.decimal_a_octal(decimal)}'))
                elif re.search(t_binario,text) is not None:
                    #Salidas.append(f'{l} Binario: {conversor.decimal_a_binario(decimal)}')
                    print((f'{l} Binario: {conversor.decimal_a_binario(decimal)}'))
                elif re.search(t_romano,text) is not None:
                    #Salidas.append(f'{l} Romano: {conversor.decimal_a_romano(decimal)}')
                    print((f'{l} Romano: {conversor.decimal_a_romano(decimal)}'))
                elif re.search(t_alternativo,text) is not None:
                    #Salidas.append(f'{l} Maya (Alternativo): {conversor.alternativo(decimal)}')
                    print((f'{l} Maya: {conversor.alternativo(decimal)}'))
                elif re.search(t_aleatorio,text) is not None:
                    if (conversor.aleatorio(decimal)!='maya'):
                        #Salidas.append(f'{l} Alteatorio: {conversor.aleatorio(decimal)}')
                        print((f'{l} Aleatorio: {conversor.aleatorio(decimal)}'))
                        


t_hexadecimal = "[H,h][E,e][X,x][A,a][D,d][E,e][C,c][I,i][M,m][A,a][L,l]"
t_octal = "[O,o][C,c][T,t][A,a][L,l]"
t_binario = "[B,b][I,i][N,n][A,a][R,r][I,i][O,o]"
t_romano = "[R,r][O,o][M,m][A,a][N,n][O,o]"
t_alternativo = "[A,a][L,l][T,t][E,e][R,r][N,n][A,a][T,t][I,i][V,v][O,o]"
t_aleatorio = "[A,a][L,l][E,e][A,a][T,t][O,o][R,r][I,i][O,o]"
t_digitos = "^\d+"
t_dolarSign="\$$"
#text = "15Octal$"
Token=[]
LinesToken=[]
NToken=0

texto=open("instrucciones.txt")
tlines=texto.readlines()
i=0
"""
"""
while(i<len(tlines)):
    text=tlines[i]
    words=text.split(' ')
    i+=1
    for j in words:
        if re.search(t_digitos,j) is not None:
            text2 = re.search(t_digitos,j)
            decimal = int(text2[0])
            Token.append(f'Linea: {i} | valor: {decimal}, Tipo: Numero Decimal')
            NToken+=1
        if re.search(t_hexadecimal,j) is not None:
            #Salida=conversor.decimal_a_hexadecimal(decimal)
            Token.append(f'Linea: {i} | valor: Hexadecimal, Tipo: Base Numerica') 
            NToken+=1 
        if re.search(t_octal,j) is not None:
            Token.append(f'Linea: {i} | valor: Octal, Tipo: Base Numerica')  
            NToken+=1
        if re.search(t_binario,j) is not None:
            Token.append(f'Linea: {i} | valor: Binario, Tipo: Base Numerica') 
            NToken+=1 
        if re.search(t_romano,j) is not None:
            Token.append(f'Linea: {i} | valor: Romano, Tipo: Base Numerica')
            NToken+=1
        if re.search(t_alternativo,j) is not None:
            Token.append(f'Linea: {i} | valor: MAYA (Base Alternativa), Tipo: Base Numerica')
            NToken+=1
        if re.search(t_aleatorio,j) is not None:
            Token.append(f'Linea: {i} | valor: Aleatorio, Tipo: Base Numerica Aleatoria')
            NToken+=1
        if re.search(t_dolarSign,j) is not None:
            Token.append(f'Linea: {i} | valor: $, Tipo: Delimitador')
            NToken+=1
    LinesToken.append(Token)
    Token=[]



ASintaxis()


