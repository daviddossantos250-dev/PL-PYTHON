#COLEÇOES EM PYTHON
#TUPLAS
#     - permitem valores duplicados
#     - são ordenadas
#     - não permitem valores mutáveis
#     - usam parênteses () para definir a coleção

#TUPLAS

#Criando uma tupla
minha_tupla = ("banana", "maçã", "laranja", "abacaxi")

#Acessando elementos da tupla
print(minha_tupla[0])
print(minha_tupla[1])
print(minha_tupla[2])
print(minha_tupla[3])
print("----------------------------------------------------")

#Modificando um elemento da tupla (isso não é permitido, pois as tuplas são imutáveis)
#minha_tupla[1] = "uva"  # Isso causará um erro
print("Não é possível modificar uma tupla, pois ela é imutável.")
print("----------------------------------------------------")

#Criando uma tupla vazia
minha_tupla_vazia = ()
print(minha_tupla_vazia)