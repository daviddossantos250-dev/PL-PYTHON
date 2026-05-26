# pedir ao utilizador palavras (uma de cada)
# escrever essas palavras num ficheiro de texto: palavras.txt
# terminar quando o utilizador digitar: "fim"
# a palavra "fim" nao dever ser armazenada no ficheiro.

import os  #biblioteca para trabalhar com caminhos de arquivos

caminho = os.path.join(os.path.dirname(__file__), "palavras.txt")
with open(caminho, mode="at", encoding="utf-8") as ficheiro:
    palavra ="" #variável para armazenar a palavra digitada pelo usuário
    while palavra.lower() != "fim":  #lower()- função para converter a palavra para minúscula, comparação com "fim"
        palavra = input("Digite uma palavra: ")  #input- função para receber a entrada do usuário
        if palavra.lower() != "fim":  #verificar se a palavra digitada é diferente de "fim"
            ficheiro.write(palavra + "\n")  #write- função para escrever no ficheiro, "\n"- quebra de linha
    print("Palavras adicionadas ao ficheiro com sucesso!")