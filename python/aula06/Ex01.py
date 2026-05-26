#JSON

import json  #importar a biblioteca json para trabalhar com arquivos JSON
import os  #importar a biblioteca os para trabalhar com caminhos de arquivos
caminho = os.path.join(os.path.dirname(__file__), "alunos.json")

with open(caminho, mode="r", encoding="utf-8") as ficheiro:  #open- função para abrir o ficheiro, "alunos.json"- nome do ficheiro a ser aberto, mode="r"- modo de abertura do ficheiro (read), encoding="utf-8"- codificação do ficheiro
    dados = json.load(ficheiro)  #json.load- função para carregar o conteúdo do ficheiro JSON em uma variável
    print("Dados carregados do ficheiro JSON:")  #imprimir mensagem indicando que os dados foram carregados
    ##print(dados)  #imprimir os dados carregados do ficheiro JSON
    print(json.dumps(dados, indent=2))  #imprimir os dados carregados do ficheiro JSON