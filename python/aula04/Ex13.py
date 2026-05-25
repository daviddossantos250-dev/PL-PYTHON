#COLEÇOES EM PYTHON
#DICIONÁRIOS
#     - permitem valores mutáveis
#     - nao permitem valores duplicados (chaves)
#     - permitem valores duplicados (valores)
#     - são ordenadas
#     - usam chave {} para definir a coleção

#DICIONÁRIOS

#Criando um dicionário
meu_dicionario = {"banana": 1, "maçã": 2, "laranja": 3, "abacaxi": 4}
print(meu_dicionario)
print("----------------------------------------------------")

#Acessando elementos do dicionário
print(meu_dicionario["banana"])
print(meu_dicionario["maçã"])
print(meu_dicionario["laranja"])
print(meu_dicionario["abacaxi"])
print("----------------------------------------------------")

#Modificando um elemento do dicionário
meu_dicionario["maçã"] = 5
print(meu_dicionario)
print("----------------------------------------------------")

#Adicionando um elemento ao dicionário
meu_dicionario["manga"] = 6
print(meu_dicionario)
print("----------------------------------------------------") 

#Removendo um elemento do dicionário
del meu_dicionario["laranja"]
print(meu_dicionario)
print("----------------------------------------------------")

#Removendo todos os elementos do dicionário
meu_dicionario.clear()
print(meu_dicionario)
print("----------------------------------------------------")
