#Variáveis
vetor = []

#Entradas
for n in range(0, 10):
    num = int(input("Informe o valor para o vetor: "))
    vetor.append(num)

#Procesamento
vetor.reverse() #inverte a lista
for n in vetor:
    print()