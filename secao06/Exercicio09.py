#Entradas
indice = float(input("Informe o índice de poluição: "))

#Processamento
if indice >= 0.3 and indice < 0.4:
    print("Atenção: Indústrias do 1º grupo devem suspender as atividades. ")
elif indice >= 0.4 and indice < 0.5:
    print("Atenção: Indústrias do 1º e 2º grupo devem suspender as atividades. ")
elif indice >= 0.5:
    print("Atenção: Todos os grupos devem suspender as atividade. ")