"""
1- Consultar uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:

> a) Imprima o resultado da soma de todos os valores da matriz no terminal;

> b) E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;
"""

import random
matriz_a=[]
matriz_b=[]
valores_b=[]
cont=0
soma=0
#criação matriz a
for i in range(1,11):
  linha=[]
  for y in range(1,11):
    linha.append(random.randint(1,8000))
  matriz_a.append(linha)
#soma dos valores e guardar valor triplicado da matriz a 
for lin in matriz_a:
  for item in lin:
    soma=soma+item
    valores_b.append(item*3) 
print("a soma dos valores dentro da matriz A é igual a: {}" .format(soma))
#criação da matriz b
for i in range(1,11):
  linha=[]
  for y in range(1,11):
    linha.append(valores_b[cont])
    cont+=1
  matriz_b.append(linha)
print("Matriz A:{}" .format(matriz_a))
print("Matriz B:{}" .format(matriz_b))