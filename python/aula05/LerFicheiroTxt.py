#ABRIR O FICHEIRO TXT

ficheiro = open("c:\\Users\\davids\\Downloads\\US\\2ºANO 2ºSEMESTRE\\PROGRAMAÇAO EM LOGICA\\python\\aula05\\alunos.txt")  #open- função para abrir o ficheiro, "alunos.txt"- nome do ficheiro a ser aberto

#ler o conteúdo do ficheiro
conteudo = ficheiro.read()  #read- função para ler o conteúdo do ficheiro
print(conteudo)  #imprimir o conteúdo do ficheiro
ficheiro.close()  #close- função para fechar o ficheiro

#ler o conteúdo do ficheiro linha por linha
ficheiro = open("c:\\Users\\davids\\Downloads\\US\\2ºANO 2ºSEMESTRE\\PROGRAMAÇAO EM LOGICA\\python\\aula05\\alunos.txt")
linhas = ficheiro.readlines()  #readlines- função para ler o conteúdo do ficheiro linha por linha e armazenar em uma lista
for linha in linhas:  #percorrer cada linha do ficheiro
    print("Linha:", linha.strip())  #strip- função para remover os espaços em branco no início e no final da linha
ficheiro.close()  #close- função para fechar o ficheiro