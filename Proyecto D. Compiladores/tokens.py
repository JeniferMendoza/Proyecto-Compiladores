from cgitb import text
import re
import Convertidor
import conversor
t_hexadecimal = "[H,h][E,e][X,x][A,a][D,d][E,e][C,c][I,i][M,m][A,a][L,l]\$$"
t_octal = "[O,o][C,c][T,t][L,l]\$$"
t_binario = "[B,b][I,i][N,n][A,a][R,r][I,i][O,o]\$$"
t_romano = "[R,r][O,o][M,m][A,a][N,n][O,o]\$$"
t_alternativo = "[A,a][L,l][T,t][E,e][R,r][N,n][A,a][T,t][I,i][V,v][O,o]\$$"
t_aleatorio = "[A,a][L,l][E,e][A,a][T,t][O,o][R,r][I,i][O,o]\$$"
t_digitos = "^\d+"
text = "123Octal"

if re.search(t_hexadecimal,text) is not None:
    print("Tipo de tocken: ")
elif re.search(t_octal,text) is not None:
   print("correcto")
elif re.search(t_binario,text) is not None:
   print("correcto")
elif re.search(t_romano,text) is not None:
   print("correcto")
elif re.search(t_alternativo,text) is not None:
   print("correcto")
elif re.search(t_aleatorio,text) is not None:
   print("correcto")
else:
    print("Vuelva a intentar")