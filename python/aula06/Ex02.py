import pandas as pd  #importar a biblioteca pandas para trabalhar com arquivos CSV
import os  #importar a biblioteca os para trabalhar com caminhos de arquivos

caminho = os.path.join(os.path.dirname(__file__), "alunos.json")
df = pd.read_json(caminho, orient="records")  #read_json- função para ler um arquivo JSON, "alunos.json"- nome do arquivo a ser lido
print(df.to_string(index=False))  #imprimir o DataFrame sem o cabeçalho (index=False) e sem os índices (index=False)