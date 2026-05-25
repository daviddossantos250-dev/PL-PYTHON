#COLEÇOES EM PYTHON
#SETS
#     - permitem valores mutáveis
#     - permitem valores duplicados
#     - são ordenadas
#     - usam chaves {} para definir a coleção

#SETS

#Criando um set
meu_set = {"banana", "maçã", "laranja", "abacaxi"}
print(meu_set)
print("----------------------------------------------------")

#Acessando elementos do set
print(meu_set[0])  # Isso causará um erro
print("----------------------------------------------------")

#Modificando um elemento do set (isso não é permitido, pois os sets são imutáveis)
#meu_set[0] = "uva"  # Isso causará um erro
print("Não é possível modificar um set, pois eles são imutáveis.")
print("----------------------------------------------------")

#Removendo um elemento do set
meu_set.remove("banana")
print(meu_set)
print("----------------------------------------------------")

#Adicionando um elemento ao set
meu_set.add("manga")
print(meu_set)
print("----------------------------------------------------")

#Removendo um elemento do set
meu_set.remove("laranja")
print(meu_set)
print("----------------------------------------------------")

#Percorrendo o set
for i in meu_set:
    print(i, end=" ")  # Imprime as frutas na mesma linha
print("----------------------------------------------------")

#Verificando se um elemento está no set
if "maçã" in meu_set:
    print("A maçã está no set.")
else:    print("A maçã não está no set.")
print("----------------------------------------------------")

#Criando um set vazio
meu_set_vazio = set()
print(meu_set_vazio)
print("----------------------------------------------------")

#Criando um set com valores duplicados
meu_set_duplicado = {"banana", "banana", "maçã", "laranja", "abacaxi"}
print(meu_set_duplicado)
print("----------------------------------------------------")

#Criando um set com uma tupla
minha_tupla = ("banana", "maçã", "laranja", "abacaxi")
meu_set_tupla = set(minha_tupla)
print(meu_set_tupla)
print("----------------------------------------------------")

#Criando um set com uma lista
minha_lista = ["banana", "maçã", "laranja", "abacaxi"]
meu_set_lista = set(minha_lista)
print(meu_set_lista)
print("----------------------------------------------------")

#Criando um set com um dicionário
meu_dicionario = {"banana": 1, "maçã": 2, "laranja": 3, "abacaxi": 4}
meu_set_dicionario = set(meu_dicionario)
print(meu_set_dicionario)
print("----------------------------------------------------")

#Criando um set com um range
meu_range = range(1, 6)
meu_set_range = set(meu_range)
print(meu_set_range)
print("----------------------------------------------------")

#Criando um set com um conjunto
meu_conjunto = {1, 2, 3, 4, 5}
meu_set_conjunto = set(meu_conjunto)
print(meu_set_conjunto)
print("----------------------------------------------------")

#Criando um set com um conjunto
meu_conjunto = {1, 2, 3, 4, 5}
meu_set_conjunto = set(meu_conjunto)
print(meu_set_conjunto)
print("----------------------------------------------------")

