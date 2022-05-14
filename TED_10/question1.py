#1 - Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.
entrada=[]
for i in range(0,20):
  i+=1
  number_entrada=int(input("Digite o {}° número\n" .format(i)))
  i-=1
  entrada.append(number_entrada)
entrada.reverse() #Resolução com função 
print(entrada)