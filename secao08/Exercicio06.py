#Variáceis
vetor = []

#Entrada
codigo = int(input("Informe o código: "))

#Processamento
if codigo != 0:
    for n in range(0, 5):
        num = float(input("Informe um valor real: "))
        vetor.append(num)
    if codigo == 1:
        for n in vetor:
            print(n)
    if codigo == 2:
        vetor.reverse()
        for n in vetor:
            print(n)
