



def menu():
    print("+-----------------------------+")
    print("| 1 - Cadastrar um novo aluno |")
    print("| 2 - Listar os alunos        |")
    print("| 3 - Editar aluno            |")
    print("| 4 - Excluir aluno           |")
    print("| 5 - Exportar para CSV       |")
    print("| 6 - Exportar para JSON      |")
    print("| 0 - Sair                    |")
    print("+-----------------------------+")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    alunos.append({"nome": nome, "idade": idade, "nota": nota})
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for i in alunos:
            print("nome: ", i["nome"], "| idade: ",i["idade"], "| nota: ",i["nota"],"|")

def editar_aluno(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        nome = input("Digite o nome do aluno que deseja editar: ")
        for i in alunos:
            if i == nome:
                

#main
alunos = []
opcao = menu()
while opcao != 0:
    if opcao == 1:
        cadastrar_aluno(alunos)
    elif opcao == 2:
        listar_alunos(alunos)
    elif opcao == 3:
        print("Editar aluno")
    elif opcao == 4:
        print("Excluir aluno")
    elif opcao == 5:
        print("Exportar para CSV")
    elif opcao == 6:
        print("Exportar para JSON")
    else:
        print("Opção inválida!")
    opcao = menu()
