#Variáveis
from secao02.Exercicio02 import num2
vetor1 = []
vetor2 = []
soma = []

#Entrada/Processamento
for n in range(0, 10):
    num1 = int(input("Informe o valor para o primeiro vetor: "))
    vetor1.append(num1)
    num2 = int(input("Informe o valor para o segundo vetor: "))
    vetor2.append(num2)
    soma.append(num1 + num2)
for n in soma:
    print(n)