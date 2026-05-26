#COLEÇOES EM PYTHON
#LISTAS
#     - permite valores duplicados
#     - permitem valores mutáveis
#     - são ordenadas
#     - usam colchetes [] para definir a coleção



#LISTAS

#Criando uma lista
minha_lista = ["banana", "maçã", "laranja", "abacaxi"]
#                0         1        2          3
#Acessando elementos da lista
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])
print(minha_lista[3])
print("----------------------------------------------------")

#Modificando um elemento da lista
minha_lista[1] = "uva"
print(minha_lista[1])
print("----------------------------------------------------")

#Adicionando um elemento à lista
minha_lista.append("manga")
print(minha_lista)
print("----------------------------------------------------")

#Removendo um elemento da lista
minha_lista.remove("laranja")
print(minha_lista)
print("----------------------------------------------------")

#Percorrendo a lista
for i in minha_lista:  
    print(i, end=" ")  # Imprime as frutas na mesma linha

for i in range (len(minha_lista)):
    print(minha_lista[i], end=" ")  # Imprime as frutas na mesma linha
print("----------------------------------------------------")

#Inserindo um elemento em uma posição específica
minha_lista.insert(1, "morango")
print(minha_lista)
print("----------------------------------------------------")

#Insertindo um elemento no final da lista
minha_lista.append("abacate")
print(minha_lista)
print("----------------------------------------------------")

#Removendo o ultimo elemento da lista
minha_lista.pop()
print(minha_lista)
print("----------------------------------------------------")

#Removendo o primeiro elemento da lista
minha_lista.pop(0)
print(minha_lista)
print("----------------------------------------------------")

#Removendo todos os elementos da lista
minha_lista.clear()
print(minha_lista)
print("----------------------------------------------------")

