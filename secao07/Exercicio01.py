#Variáveis
maior = 0

#Entrada
n = int(input("Informe um número"))
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Informe um número: "))
print("O maior número e {0}".format(maior))
