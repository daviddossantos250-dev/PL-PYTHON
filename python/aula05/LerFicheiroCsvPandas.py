#FICHEIRO CSV USANDO PANDAS
#INSTALAÇÃO DA BIBLIOTECA PANDAS NO TERMINAL: pip install pandas


import pandas as pd  #importar a biblioteca pandas para trabalhar com arquivos CSV
import os  #importar a biblioteca os para trabalhar com caminhos de arquivos


caminho = os.path.join(os.path.dirname(__file__), "alunos.csv")
df = pd.read_csv(caminho, delimiter=",")  #read_csv- função para ler um arquivo CSV, "alunos.csv"- nome do arquivo a ser lido
print(df)  #imprimir o DataFrame