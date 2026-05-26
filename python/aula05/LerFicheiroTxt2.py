import os


# Ler um ficheiro de texto.
#with- função para abrir o ficheiro, "aula05/alunos.txt"- nome do ficheiro a ser aberto, mode="at"- modo de abertura do ficheiro (append text), encoding="utf-8"- codificação do ficheiro

# Caminho relativo - funciona sempre que o script estiver em aula05/
caminho = os.path.join(os.path.dirname(__file__), "alunos.txt")
with open (caminho, mode="at", encoding="utf-8") as ficheiro:
    texto = input("Digite o nome do aluno: ")  #input- função para receber a entrada do usuário
    ficheiro.write(texto + "\n")  #write- função para escrever no ficheiro, "\n"- quebra de linha
print("Aluno adicionado ao ficheiro com sucesso!")

# Ler o conteúdo do ficheiro
conteudo = open(caminho, mode="rt", encoding="utf-8").read()  #open- função para abrir o ficheiro, mode="rt"- modo de abertura do ficheiro (read text), encoding="utf-8"- codificação do ficheiro, read()- função para ler o conteúdo do ficheiro
print("Conteúdo do ficheiro:\n", conteudo)  #imprimir o conteúdo do ficheiro