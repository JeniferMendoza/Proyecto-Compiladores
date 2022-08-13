import re
from traceback import print_list
import conversor
error=[]
ErrorLines=[]

#Analisis de sintaxis. Verifica si cada instruccion está ingresada de manera correxta.
def ASintaxis():
    Exp=re.compile('^\d+\s+\w+\s+\$\n*$')
    texto=open("instrucciones.txt")
    tlines=texto.readlines()
    i=0
    resultado=[]
    while(i<len(tlines)):
        text=tlines[i]
        i+=1
        if Exp.match(text) is not None:
            resultado.append(f'{i}: '+str(LinesToken[i-1]))
        else:
            if(text=="" or text=='\s' or text=='\n'):
                #Si la linea está vacia pasar
                pass
            else:
                ErrorLines.append(i)
                words=text.split(' ')
                if(len(words)==1):
                    if re.search(t_digitos,words[0]) is None: 
                        error.append(f"Error de sintaxis en la linea {i}, {words[0]} no identificado, se esperaba un decimal y una base numerica.")
                    else:
                        error.append(f"Error de sintaxis en la linea {i}, se esperaba un decimal y una base numerica.")
                elif(len(words)==2):
                    if re.search(t_digitos,words[0]) is None: 
                        error.append(f"Error de sintaxis en la linea {i}, {words[0]} no identificado, se esperaba un decimal.")
                    elif re.search(t_aleatorio,words[1]) is None and re.search(t_alternativo,words[1]) is None and re.search(t_binario,words[1]) is None and re.search(t_hexadecimal,words[1]) is None and re.search(t_octal,words[1]) is None and re.search(t_romano,words[1]) is None:
                        error.append(f"Error de sintaxis en la linea {i}, {words[1]} no identificado, se esperaba una base numerica permitida.")
                    else:
                        error.append(f"Error de sintaxis en la linea {i}, {words[0]} {words[1]} no identificado, se esperaba $ al final de la linea.")
                elif(len(words)==3):
                    if re.search(t_digitos,words[0]) is None: 
                        error.append(f"Error de sintaxis en la linea {i}, {words[0]} no identificado, se esperaba un decimal.")
                    elif re.search(t_aleatorio,words[1]) is None and re.search(t_alternativo,words[1]) is None and re.search(t_binario,words[1]) is None and re.search(t_hexadecimal,words[1]) is None and re.search(t_octal,words[1]) is None and re.search(t_romano,words[1]) is None:
                        error.append(f"Error de sintaxis en la linea {i}, {words[1]} no identificado, se esperaba una base numerica permitida.")
                    elif re.search(t_dolarSign,words[2]) is None:
                        error.append(f"Error de sintaxis en la linea {i}, {words[2]} no identificado, se esperaba $ al final de la linea")
                else:
                    error.append(f"Error de sintaxis en la linea {i}, entrada no identificada.")
    MostrarResultados()

def MostrarResultados():
    print('Resultados: \n')
    HacerConversiones()
    print('\n')
    print('Errores Encontrados: \n')
    line=1
    for i in error:
        print ("{:<3} {:<30}".format(line,i))
        line+=1
    print('\n')
    print(f'TOKENS Encotrados: {NToken}')
    print ("{:<15} {:<15} {:<15}".format('Linea','Valor','Tipo de Token'))
    for i in LinesToken:
        a=0
        while(a<len(i)):
            print ("{:<3} {:<15} {:<15}".format( i[a][0], i[a][1], i[a][2]))
            a+=1
    

def HacerConversiones():
    l=0
    while(l<len(tlines)):
        text=tlines[l]
        l+=1
        if(l in ErrorLines):
            print(f'{l}: Error. Error de Sintaxis en la linea {l}')
        else:
            if re.search(t_digitos,text) is not None:
                text2 = re.search(t_digitos,text)
                decimal = int(text2[0])
                if re.search(t_hexadecimal,text) is not None:
                    print((f'{l} Hexadecimal: {conversor.decimal_a_hexadecimal(decimal)}'))
                elif re.search(t_octal,text) is not None:
                    print((f'{l} Octal: {conversor.decimal_a_octal(decimal)}'))
                elif re.search(t_binario,text) is not None:
                    print((f'{l} Binario: {conversor.decimal_a_binario(decimal)}'))
                elif re.search(t_romano,text) is not None:
                    print((f'{l} Romano: {conversor.decimal_a_romano(decimal)}'))
                elif re.search(t_alternativo,text) is not None:
                    print(f'{l} Maya: ')
                    conversor.alternativo(decimal)
                elif re.search(t_aleatorio,text) is not None:
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
        L=[]
        if re.search(t_digitos,j) is not None:
            text2 = re.search(t_digitos,j)
            decimal = int(text2[0])
            L.append(f'{i}')
            L.append(f'{decimal}')
            L.append('Numero Decimal')
            Token.append(L)
            NToken+=1
        if re.search(t_hexadecimal,j) is not None:
            #Salida=conversor.decimal_a_hexadecimal(decimal)
            L.append(f'{i}')
            L.append('Hexadecimal')
            L.append('Base Numerica')
            Token.append(L)
            NToken+=1 
        if re.search(t_octal,j) is not None:
            L.append(f'{i}')
            L.append('Octal')
            L.append('Base Numerica')
            Token.append(L)  
            NToken+=1
        if re.search(t_binario,j) is not None:
            L.append(f'{i}')
            L.append('Binario')
            L.append('Base Numerica')
            Token.append(L)
            NToken+=1 
        if re.search(t_romano,j) is not None:
            L.append(f'{i}')
            L.append('Romano')
            L.append('Base Numerica')
            Token.append(L)
            NToken+=1
        if re.search(t_alternativo,j) is not None:
            L.append(f'{i}')
            L.append('Maya')
            L.append('Base Numerica')
            Token.append(L)
            NToken+=1
        if re.search(t_aleatorio,j) is not None:
            L.append(f'{i}')
            L.append('Alteatorio')
            L.append('Base Numerica Aleatoria')
            Token.append(L)
            NToken+=1
        if re.search(t_dolarSign,j) is not None:
            L.append(f'{i}')
            L.append('$')
            L.append('Delimitador de Linea')
            Token.append(L)
            NToken+=1
    LinesToken.append(Token)
    Token=[]



ASintaxis()


