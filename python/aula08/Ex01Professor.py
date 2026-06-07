#ENUNCIADO
#App em python para gestao de alunos (CRUD)
#Exportar para CSV e JSON

#Criar uma classe Aluno com os atributos nome, idade e nota.
class Aluno:
    def __init__(self, nome, idade, nota): #construtor com parametros
        self.nome = nome  
        self.idade = idade
        self.nota = nota

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
    aluno = Aluno(nome, idade, nota) #cria um objeto aluno
    alunos.append(aluno) #adiciona o objeto aluno na lista de alunos
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("Nome:", aluno.nome, "Idade:", aluno.idade, "Nota:", aluno.nota)


def editar_aluno(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        listar_alunos(alunos) #lista os alunos para o usuario escolher qual aluno deseja editar
        nome = input("Digite o nome do aluno que deseja editar: ")
        for aluno in alunos:
            while aluno.nome == nome:
                print("Oque pretende editar?")
                print("1 - Nome")
                print("2 - Idade")
                print("3 - Nota")
                while True:
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao == 1:
                        nome = input("Digite o novo nome do aluno: ")
                        aluno.nome = nome
                        print("Aluno editado com sucesso!")
                        break
                    elif opcao == 2:
                        idade = int(input("Digite a nova idade do aluno: "))
                        aluno.idade = idade
                        print("Aluno editado com sucesso!")
                        break
                    elif opcao == 3:
                        nota = float(input("Digite a nova nota do aluno: "))
                        aluno.nota = nota
                        print("Aluno editado com sucesso!")
                        break
                    else:
                        print("Opção inválida!")
                return
        print("Aluno não encontrado.")


alunos = []
opcao = menu()
while opcao != 0:
    match opcao:
        case 1:
            cadastrar_aluno(alunos)
        case 2:
            listar_alunos(alunos)
        case 3:
            editar_aluno(alunos)
        case 4:
            print("Excluir aluno")
        case 5:
            print("Exportar para CSV")
        case 6:
            print("Exportar para JSON")
        case _:
            print("Opção inválida!")
    opcao = menu()