import csv  #importar a biblioteca csv para trabalhar com arquivos CSV
import os  #importar a biblioteca os para trabalhar com caminhos de arquivos

caminho = os.path.join(os.path.dirname(__file__), "alunos.csv")
with open(caminho, mode="rt", encoding="utf-8") as ficheiro:  #open- função para abrir o ficheiro, "alunos.csv"- nome do ficheiro a ser aberto, mode="rt"- modo de abertura do ficheiro (read text), encoding="utf-8"- codificação do ficheiro
    leitor = csv.reader(ficheiro, delimiter=",")  #csv.reader- função para criar um leitor CSV
    for linha in leitor:  #percorrer cada linha do ficheiro
        print(linha)  #imprimir a linha do ficheiro