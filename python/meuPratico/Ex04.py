
#Exercício 1: Usando while, pede números ao utilizador repetidamente até ele escrever 0. No final mostra a soma de #todos os números inseridos.
#Exercício 2: Usando for e range(), mostra a tabuada de um número à escolha do utilizador (de 1 a 10).
#Exercício 3: Usando for, percorre a palavra "Cabo Verde" e conta quantas vogais tem. Mostra o resultado no final.



soma = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")




numero = int(input("Qual é a tabuada que queres ver? "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



palavra = "Cabo Verde"
vogais = "aeiouAEIOU"
i = 0
contador_vogais = 0
for i in palavra:
    contador_vogais += i in vogais
print(contador_vogais)

#ou

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
print(contador_vogais)