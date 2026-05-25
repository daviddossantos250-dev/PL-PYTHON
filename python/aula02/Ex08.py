# funcao sem parametros
def sabura():
    #corpo da funcao
    print("li keh terra!!!")
#fim da funcao

#chamar a funcao
sabura()
sabura()

#criar uma funcao que recebe parametros
def soma(a,b):
    res = a + b
    print(a," + ",b," = ", res)
#fim da funcao

#chamar a funcao
soma(2,3)

#funcao que recebe parametros opcionais
def ottuSoma(a,b=1):
    res = a + b
    print(a," + ",b," = ", res)
#fim da funcao

#chamar a funcao
ottuSoma(3)
ottuSoma(3,5)

#funcao que recebe valores opcionais, sem valor por omissao
def sigiSabura(texto, ottu=None):
    if(ottu is None):
        print("sabura di ",texto)
    else:
        print("sabura di ",texto," teh ", ottu)
#fim funcao

#chamar a funcao
sigiSabura("praia","somada")

#funcao que devolve valor
def multipicar(a,b):
    return a*b
#fim da funcao

#chamar a funcao
res = multipicar(2,3)
print("res: ", res)