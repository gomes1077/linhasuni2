import math
import cmath
import os
from tkinter import*
import matplotlib.pyplot as plt

vs = 10
rs=30
zo=50
vp=2.01*(10**8)
zl=150
l=0.1
tg=2*10**-9
tgraf=0
resto=0

#encontrando corrente e tensão inicial

io = vs/(rs+zo)
vo = (zo/(rs+zo))*vs
print(io)
print(vo)

#encontrando a velocidade de propagação com c

u=vp
print(u)

#encontrando o tempo de alcance das ondas nas cargas

ti = l/u
print(ti)

#encontrando o coeficiente de reflexão da tensão no gerador e na carga

rg=(rs-zo)/(rs+zo)
rc=(zl-zo)/(zl+zo)
print(rg)
print(rc)

#encontrando quantos pontos terá a reflexão

p = tg/ti
print(p)

tt=tg/p
print(tt)

ttnovo=0

#lista de tensões para grafico e definindo os pontos da função em x conforme os pontos 

lista_tensao_grafico = []
lista_pontos_grafico = []

ant=0

for i in range(0, int(p)+1):
  if i % 2 == 0:
    resto = True
    sinal = -1
  else:
    resto = False
  if (i % 4 == 0):
    sinal = 1

  #funções da questão 2

  if (i==0):
    tgraf = vo
    sinal = 1
  if (resto==False):
    if (i==1):
      ac=1
    if (i!=1):
      ac=0
    tgraf=tgraf+(sinal*vo*(rc**((i+ac)/2))*(rg**(i-1)))
  if ((resto==True) and (i!=0)):
    tgraf=tgraf+(sinal*vo*(rc**(i-1))*(rg**(i/2)))
  lista_tensao_grafico.append(tgraf)
  lista_tensao_grafico.append(tgraf)
  if (i==0):
    lista_pontos_grafico.append((tt*i))
  if (i!=0):
    lista_pontos_grafico.append((tt*i))
    lista_pontos_grafico.append((tt*i))
else:

  lista_pontos_grafico.insert(10,tt*i )
  print(lista_tensao_grafico)
  print(lista_pontos_grafico)
  plt.scatter(lista_pontos_grafico,lista_tensao_grafico)
  plt.plot(lista_pontos_grafico,lista_tensao_grafico)
