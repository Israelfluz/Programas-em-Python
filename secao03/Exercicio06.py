#netradas
valor_por_hora = float(input("Qual o valor que você ganha por hora?"))
horas_trabalhandas = int(input("Quantas horas você trabalhou neste mês:"))

#Processamento
salario = horas_trabalhandas * valor_por_hora

#Saída
print("Neste mês você vai receber R$ {0: .2f}".format(salario))
