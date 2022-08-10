
def decimal_a_maya(numero):
  numero = int(input())
  simb0 = "Ჶ"
  simb1 = "•"
  simb5 = "ꟷꟷꟷꟷ"
  b = numero
  c = 1
  cont = 1
  f = []
  d = 1
  k = 0
  g = 0

  while c>=1:
    b = b/20
    if b>1:
        cont += 1
    elif b==1:
        cont += 1
    else:
        c = 0
  b=numero
  if b == 0:
    f.append(b) 

  while cont!=0:
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
    num = f[k]
    if num == 0:
        print(simb0)

    while num != 0:
        if num > 4:
            e=num%5
            g = int((num-e)/5)
            num=e
        else:
            for i in range(num):
                print(simb1, end="")
            print()
            num=0
    for i in range(g):
        print(simb5)
    print()
    k+=1



print(decimal_a_maya(0))


