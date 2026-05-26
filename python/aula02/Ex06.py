# ciclo for em java
# for (int i = 0; i<10; i++)

for letra in "us riba la":
    print(letra)

#range(ini, fim)
for i in range(0,10):
    print("volta: ",i)

nome = input("como te chamas?")
for i in nome:
    print(i,end=" ")


#########################################################################################
#FOR
print("---Ciclo For---")
for letra in "Python": #percorre cada caractere da string "Python"
    print(letra)
#FIM DO FOR

#RANGE
print("---Ciclo Range---")
for i in range(10): #range(10) gera uma sequência de números de 0 a 9
    print("Volta: ",i)
#FIM DO RANGE

nome = input("Digite seu nome: ")
for letra in nome:
    print(letra, end=" ")#end=" " para não quebrar a linha
#FIM DO FOR