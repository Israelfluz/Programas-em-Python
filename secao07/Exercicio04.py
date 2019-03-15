#Variáveis
maior = -999
menor = 999
soma = 0

#Entrada/processamento 
for n in range(1, 11):
    valor = int(input("Informe um valor: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Informe um valor: "))
media = soma / 10

#Saída
print("O maior número é {0}".format(maior))
print("O menor número é {0}".format(menor))
print("O média dos números é {0}".format(media))