#Entrada
numero = int(input("Informe um núemro entre 1 e 10: "))

#Processamento
while numero < 1 or numero > 10:
    numero = int(input("Informe um número entre 1 e 10: "))
for n in range(1, 11):
    print("{0} x {1} = {2}".format(numero, n,(numero * n)))