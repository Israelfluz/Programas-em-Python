#Entradas
nome = input("informe o nome: ")
senha = input("Informe a senha: ")

#Processamento
while nome == senha:
    print("Nome de usuário e senha devem ser diferentes.")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")
    