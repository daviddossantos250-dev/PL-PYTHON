
#Exercício 1: Pede uma nota (0–100) ao utilizador e mostra a classificação:

#90–100 → "Excelente"
#75–89 → "Bom"
#60–74 → "Suficiente"
#abaixo de 60 → "Reprovado"

#Exercício 2: Pede ao utilizador um número e diz se é positivo, negativo ou zero.
#Exercício 3: Pede o nome de um país. Se for "Cabo Verde", mostra "Bem-vindo a #casa!". Se for "Portugal", mostra "Boa viagem para a metrópole!". Para qualquer #outro, mostra "Destino desconhecido.".


nota = int(input("Digite a nota de 0 a 100: "))

if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 75 and nota < 90:
    print("Bom")
elif nota >= 60 and nota < 75:
    print("Suficiente")
elif nota < 60:
    print("Reprovado")


numero = int(input("Digite um número: "))
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")



pais = input("Digite o nome de um país: ")
if pais == "Cabo Verde":
    print("Bem-vindo a casa!")
elif pais == "Portugal":
    print("Boa viagem para a metrópole!")
else:
    print("Destino desconhecido.")