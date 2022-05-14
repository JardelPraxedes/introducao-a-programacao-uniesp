#2 - Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.
repetidos=0
entrada_number=[]
for i in range(0,50):
  i+=1
  inserir=int(input("digite o {}° número:\n" .format(i)))
  i-=1
  entrada_number.append(inserir)
entrada_number.sort() #função que ordena valores em ordem crescente
print("Lista dos valores do vetor: {}" .format(entrada_number))
for i in range(0, len(entrada_number)-1): #
  if entrada_number[i]==(entrada_number[i+1]): #compara o valor do indice atual com o próximo. Por isso "-1" no for 
    repetidos+=1
    a = entrada_number[i]
    b =entrada_number[i+1]
    print("o valor {} está se repetindo e ambos se localizam na {}° e {}° posição do vetor" .format(entrada_number[i], entrada_number.index(a) ,entrada_number.index(b)+1))
    entrada_number[i]="check" #esse valor do vetor já foi utilizado e printado, substitui por outro valor que não esteja no vetor, pois 2 valores númericos iguais a função index exibe o mesmo indice
print("Total de repetições: {}" .format(repetidos))


