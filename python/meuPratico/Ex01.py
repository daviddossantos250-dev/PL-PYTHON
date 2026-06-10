#Exercício 1: Cria variáveis para guardar o teu nome, idade, cidade e se és #estudante (True/False). Mostra tudo com uma f-string numa só linha.
#Exercício 2: Pede ao utilizador o nome e a idade. Mostra uma mensagem como:
#Olá, David! Tens 20 anos.
#Exercício 3: Pede ao utilizador dois números e mostra a soma. Lembra-te de #converter o input() para int!

nome = input("Digite seu nome: ")
idade = input ("Digite sua idade: ")
cidade = input ("Digite sua cidade: ")
estudante = input("Você é estudante? ")

if estudante == "true":
    print(f"Olá {nome}, você tem {idade} anos, mora em {cidade} e é estudante.")
else:    
    print(f"Olá {nome}, você tem {idade} anos, mora em {cidade} e não é estudante.")

nome = input("Digite seu nome: ")
idade = input ("Digite sua idade: ")
print(f"Olá {nome}! Você tem {idade} anos.")


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: ")) 

soma = numero1 + numero2
print(f"Olá {nome}, a soma dos números é: {soma}")