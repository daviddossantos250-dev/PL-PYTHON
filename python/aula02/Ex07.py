#somatorio de n-primeiros numeros
# numero fornecido pelo utilizador
n = int(input("indique um numero: "))
soma = 0
#for i in range(1, n + 1):
#    soma += i
#print("somatorio: ",soma)

i=1
while i<= n:
    soma = soma + i  # soma += i
    i = i + 1        # i += 1
print("somatorio: ",soma)


##########################################################################

#SOMATORIO DE N-PRIMEIROS NUMEROS
#NUMERO FORNECIDO PELO USUÁRIO
print("---SOMATORIO DE N-PRIMEIROS NUMEROS---")
n = int(input("Digite um número: "))
soma = 0
for i in range(1, n+1): #range(1, n+1) gera uma sequência de números de 1 a n
    soma += i #soma = soma + i
print("Soma dos primeiros", n, "números: ", soma)

#COM WHILE
print("---SOMATORIO DE N-PRIMEIROS NUMEROS COM WHILE---")
n = int(input("Digite um número: "))
soma = 0
i = 1
while i <= n:
    soma += i #soma = soma + i
    i += 1
print("Soma dos primeiros", n, "números: ", soma)